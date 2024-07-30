from aiogram import F, types, Router
from aiogram.filters import StateFilter, or_f, Filter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keybords import kbd

hndl_spis_literature_router = Router()


class literature():
    def __init__(self):
        self.surname_main = "" #Фамилия осн автора
        self.name1_main = "" #1-ый инициал осн автора
        self.name2_main = ""#2-ой инициал осн автора
        self.surname_additive1 = ""
        self.name1_additive1 = ""
        self.name1_additive2 = ""
        self.surname_additive2 = ""
        self.name2_additive1 = ""
        self.name2_additive2 = ""
        self.name_of_literature = ""
        self.city = ""
        self.place_of_publication = ""
        self.year = ""
        self.pages = ""
        self.reference = ""
    def spis_for_less_4_authors(self):
        return (f"{self.surname_main}, {self.name1_main} {self.name2_main} {self.name_of_literature} /"
                f" {self.name1_main} {self.name2_main} {self.surname_main} - {self.city} : {self.place_of_publication}, {self.year}. - {self.pages} c. ")
    def spis_for_2_authors(self):
        return (f"{self.surname_main}, {self.name1_main} {self.name2_main} {self.name_of_literature} /"
                f" {self.name1_main} {self.name2_main} {self.surname_main}, {self.surname_additive1} {self.name1_additive1}. {self.name1_additive2}."
                f" - {self.city} : {self.place_of_publication}, {self.year}. - {self.pages} c. ")
    def spis_for_3_authors(self):
        return (f"{self.surname_main}, {self.name1_main} {self.name2_main} {self.name_of_literature} /"
                f" {self.name1_main} {self.name2_main} {self.surname_main}, {self.surname_additive1} {self.name1_additive1}. {self.name1_additive2},"
                f"{self.surname_additive2} {self.name2_additive1}. {self.name2_additive2} ."
                f" - {self.city} : {self.place_of_publication}, {self.year}. - {self.pages} c. ")
    def spis_for_more_4_authors(self):
        return (f"{self.name_of_literature} / {self.surname_main} {self.name1_main} {self.name2_main} [и др.]."
                f" - {self.city} : {self.place_of_publication}, {self.year} - {self.pages} c.")
    def spis_for_far_electr_resourses(self):
        return (f"{object.name_of_literature} [Электронный ресурс]. - Режим доступа: {object.reference}. - Дата доступа: {object.year}.")

class shablony(StatesGroup):
    surname_main = State()
    name1_main = State()
    name2_main = State()
    surname_additive1 = State()
    name1_additive1 = State()
    name1_additive2 = State()
    surname_additive2 = State()
    name2_additive1 = State()
    name2_additive2 = State()
    name_of_literature = State()
    city = State()
    place_of_publication = State()
    year = State()
    pages = State()
    reference = State()

object = literature()

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == 'оформить список литературы')
async def answer(message: types.message, state=FSMContext):
    await message.answer("Для оформления нужно ввести все данные\n"
                         "Введите фамилию основного автора издания", reply_markup=kbd.end_kb)
    await state.set_state(shablony.surname_main)


@hndl_spis_literature_router.message(shablony.surname_main, F.text)
async def answer(message: types.message, state=FSMContext):
    object.surname_main = message.text
    await message.answer("Напишите первый инициал основного автора с точкой")
    await state.set_state(shablony.name1_main)


@hndl_spis_literature_router.message(shablony.name1_main, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name1_main = message.text
    await message.answer("Напишите второй инициал основного автора с точкой")
    await state.set_state(shablony.name2_main)

@hndl_spis_literature_router.message(shablony.name2_main, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name2_main = message.text
    await message.answer("Напишите фамилию первого соавтора издания")
    await state.set_state(shablony.surname_additive1)

@hndl_spis_literature_router.message(shablony.surname_additive1, F.text)
async def answer(message: types.message, state=FSMContext):
    object.surname_additive1 = message.text
    await message.answer("Напишите первый инициал первого соавтора с точкой")
    await state.set_state(shablony.name1_additive1)

@hndl_spis_literature_router.message(shablony.name1_additive1, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name1_additive1 = message.text
    await message.answer("Напишите второй инициал первого соавтора с точкой")
    await state.set_state(shablony.name1_additive2)

@hndl_spis_literature_router.message(shablony.name1_additive2, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name1_additive2 = message.text
    await message.answer("Напишите фамилию второго соавтора")
    await state.set_state(shablony.surname_additive2)

@hndl_spis_literature_router.message(shablony.surname_additive2, F.text)
async def answer(message: types.message, state=FSMContext):
    object.surname_additive2 = message.text
    await message.answer("Напишите первый инициал второго соавтора с точкой")
    await state.set_state(shablony.name2_additive1)

@hndl_spis_literature_router.message(shablony.name2_additive1, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name2_additive1 = message.text
    await message.answer("Напишите второй инициал второго соавтора с точкой")
    await state.set_state(shablony.name2_additive2)

@hndl_spis_literature_router.message(shablony.name2_additive2, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name2_additive2 = message.text
    await message.answer("Напишите название источника")
    await state.set_state(shablony.name_of_literature)

@hndl_spis_literature_router.message(shablony.name_of_literature, F.text)
async def answer(message: types.message, state=FSMContext):
    object.name_of_literature = message.text
    await message.answer("Напишите город издательства")
    await state.set_state(shablony.city)

@hndl_spis_literature_router.message(shablony.city, F.text)
async def answer(message: types.message, state=FSMContext):
    object.city = message.text
    await message.answer("Напишите место издательства")
    await state.set_state(shablony.place_of_publication)

@hndl_spis_literature_router.message(shablony.place_of_publication, F.text)
async def answer(message: types.message, state=FSMContext):
    object.place_of_publication = message.text
    await message.answer("Напишите год издания(либо дату доступа, если нужно оформить эл.ресурс")
    await state.set_state(shablony.year)


@hndl_spis_literature_router.message(shablony.year, F.text)
async def answer(message: types.message, state=FSMContext):
    object.year = message.text
    await message.answer("Напишите количество страниц")
    await state.set_state(shablony.pages)


@hndl_spis_literature_router.message(shablony.pages, F.text)
async def answer(message: types.message, state=FSMContext):
    object.pages = message.text
    await message.answer("Вставьте ссылку на источник")
    await state.set_state(shablony.reference)


@hndl_spis_literature_router.message(shablony.reference, F.text)
async def answer(message: types.message, state=FSMContext):
    object.reference = message.text
    await state.clear()
    await message.answer("Все данные собраны!", reply_markup=kbd.litrature_kb)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "издания до 4-ех авторов")
async def answer(message: types.message):
    await message.answer("Сколько авторов у источника?", reply_markup=kbd.literature_more_1_author)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "один автор")
async def answer(message: types.message):
    await message.answer(object.spis_for_less_4_authors(), reply_markup=kbd.end_kb)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "два автора")
async def answer(message: types.message):
    await message.answer(object.spis_for_2_authors(), reply_markup=kbd.end_kb)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "три автора")
async def answer(message: types.message):
    await message.answer(object.spis_for_3_authors(), reply_markup=kbd.end_kb)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "издания более 4-ех авторов")
async def answer(message: types.message):
    await message.answer(object.spis_for_more_4_authors(), reply_markup=kbd.end_kb)

@hndl_spis_literature_router.message(StateFilter(None), F.text.lower() == "эл. ресурсы удаленного доступа")
async def answer(message: types.message):
    await message.answer(object.spis_for_far_electr_resourses(), reply_markup=kbd.end_kb)



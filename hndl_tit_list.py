from aiogram import F, types, Router
import os
from datetime import date
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from docxtpl import DocxTemplate
from aiogram.fsm.state import StatesGroup, State
from keybords import kbd

Kafedra = ""
Specialization = ""
Discipline = ""
Topic = ""
Group = ""
Number = ""
Std = ""
Prepod = ""
Degree = ""

today = date.today()
doc = DocxTemplate("assets/titullnik.docx")
hndl_tit_list_router = Router()

class Decor_tit_List(StatesGroup):
    kafedra = State()
    specialization = State()
    discipline = State()
    topic = State()
    group = State()
    number = State()
    name_std = State()
    name_prepod = State()
    degree = State()
    zvanie = State()

@hndl_tit_list_router.message(StateFilter(None), F.text.lower() == 'оформить титульный лист')
async def button_tit_list(message: types.message, state=FSMContext):
    await message.answer("Напишите название вашей кафедры", reply_markup=kbd.end_kb)
    await state.set_state(Decor_tit_List.kafedra)

@hndl_tit_list_router.message(Decor_tit_List.kafedra, F.text)
async def vvod_kafedra_set_specialization(message: types.message, state=FSMContext):
    global Kafedra
    Kafedra = message.text
    await state.update_data(kafedra=message.text)
    await message.answer("Напишите название вашей специальности")
    await state.set_state(Decor_tit_List.specialization)

@hndl_tit_list_router.message(Decor_tit_List.specialization, F.text)
async def vvod_specialization_set_discipline(message: types.message, state=FSMContext):
    global Specialization
    Specialization = message.text
    await state.update_data(specialization=message.text)
    await message.answer("Напишите название вашей дисциплины")
    await state.set_state(Decor_tit_List.discipline)

@hndl_tit_list_router.message(Decor_tit_List.discipline, F.text)
async def vvod_discipline_set_topic(message: types.message, state=FSMContext):
    global Discipline
    Discipline = message.text
    await state.update_data(discipline=message.text)
    await message.answer("Напишите название вашей темы")
    await state.set_state(Decor_tit_List.topic)

@hndl_tit_list_router.message(Decor_tit_List.topic, F.text)
async def vvod_topic_set_group(message: types.message, state=FSMContext):
    global Topic
    Topic = message.text
    await state.update_data(topic=message.text)
    await message.answer("Напишите название вашей группы (Пример: УИР-1)")
    await state.set_state(Decor_tit_List.group)

@hndl_tit_list_router.message(Decor_tit_List.group, F.text)
async def vvod_group_set_number(message: types.message, state=FSMContext):
    global Group
    Group = message.text
    await state.update_data(group=message.text)
    await message.answer("Напишите номер вашего курса")
    await state.set_state(Decor_tit_List.number)
@hndl_tit_list_router.message(Decor_tit_List.number, F.text)
async def vvod_number_set_name_std(message: types.message, state=FSMContext):
    global Number
    Number = message.text
    await state.update_data(number=message.text)
    await message.answer("Напишите ваше имя (Пример: И. И. Иванов)")
    await state.set_state(Decor_tit_List.name_std)

@hndl_tit_list_router.message(Decor_tit_List.name_std, F.text)
async def vvod_name_std_set_name_prepod(message: types.message, state=FSMContext):
    global  Std
    Std = message.text
    await state.update_data(name_std=message.text)
    await message.answer("Напишите имя вашего преподавателя(Пример: И. И. Иванов)")
    await state.set_state(Decor_tit_List.name_prepod)

@hndl_tit_list_router.message(Decor_tit_List.name_prepod, F.text)
async def vvod_name_prepod_set_degree(message: types.message, state=FSMContext):
    global Prepod
    Prepod = message.text
    await state.update_data(name_prepod=message.text)
    await message.answer("Напишите начную степень вашего преподавателя (Пример: Кандидат экономических наук)")
    await state.set_state(Decor_tit_List.degree)

@hndl_tit_list_router.message(Decor_tit_List.degree, F.text)
async def vvod_degree_set_zvanie(message: types.message, state=FSMContext):
    global  Degree
    Degree = message.text
    await state.update_data(degree=message.text)
    await message.answer("Напишите начное звание вашего преподавателя (Пример: Доцент)")
    await state.set_state(Decor_tit_List.zvanie)

@hndl_tit_list_router.message(Decor_tit_List.zvanie, F.text)
async def vvod_zvanie(message: types.message, state=FSMContext):
    context = {
        'kafedra': Kafedra,
        'specialization': Specialization,
        'discipline': Discipline,
        'topic': Topic,
        'group': Group,
        'number': Number,
        'std': Std,
        'prepod': Prepod,
        'degree': Degree,
        'zvanie': message.text,
        'year': today.year
    }
    doc.render(context)
    await state.update_data(zvanie=message.text)
    await message.answer("Ваш титульный лист готов!", reply_markup=kbd.tit_list_kb)
    await state.clear()

@hndl_tit_list_router.message(F.text.lower() == 'получить файл')
async def file_docx_tit_list(message: types.message):
    doc.save("tit_list.docx")
    await message.answer_document(types.FSInputFile(r'tit_list.docx'),
                                  reply_markup=kbd.start_kb)
    os.remove("tit_list.docx")

    from docx import Document
    from docx.shared import Pt

    doc = Document()
    # задаем стиль текста по умолчанию
    style = doc.styles['Normal']
    # название шрифта
    style.font.name = 'Arial'
    # размер шрифта
    style.font.size = Pt(14)
    document.add_paragraph('Текст документа')

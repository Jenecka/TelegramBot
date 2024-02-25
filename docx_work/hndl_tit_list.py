from aiogram import F, types, Router
import os
from datetime import date
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from docxtpl import DocxTemplate
from aiogram.fsm.state import StatesGroup, State
from keybords import kbd

today = date.today()
doc = DocxTemplate("assets/main_sheet.docx")
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
    context = {'kafedra': F.text}
    doc.render(context)
    await message.answer("Напишите название вашей специальности")
    await state.set_state(Decor_tit_List.specialization)

@hndl_tit_list_router.message(Decor_tit_List.specialization, F.text)
async def vvod_specialization_set_discipline(message: types.message, state=FSMContext):
    context = {'specialization': F.text}
    doc.render(context)
    await message.answer("Напишите название вашей дисциплины")
    await state.set_state(Decor_tit_List.discipline)

@hndl_tit_list_router.message(Decor_tit_List.discipline, F.text)
async def vvod_discipline_set_topic(message: types.message, state=FSMContext):
    context = {'discipline': F.text}
    doc.render(context)
    await message.answer("Напишите название вашей темы")
    await state.set_state(Decor_tit_List.topic)

@hndl_tit_list_router.message(Decor_tit_List.topic, F.text)
async def vvod_topic_set_group(message: types.message, state=FSMContext):
    context = {'topic': F.text}
    doc.render(context)
    await message.answer("Напишите название вашей группы (Пример: УИР-1)")
    await state.set_state(Decor_tit_List.group)

@hndl_tit_list_router.message(Decor_tit_List.group, F.text)
async def vvod_group_set_number(message: types.message, state=FSMContext):
    context = {'group': F.text}
    doc.render(context)
    await message.answer("Напишите номер вашего курса")
    await state.set_state(Decor_tit_List.number)
@hndl_tit_list_router.message(Decor_tit_List.number, F.text)
async def vvod_number_set_name_std(message: types.message, state=FSMContext):
    context = {'number': F.text}
    doc.render(context)
    await message.answer("Напишите ваше имя (Пример: И. И. Иванов)")
    await state.set_state(Decor_tit_List.name_std)

@hndl_tit_list_router.message(Decor_tit_List.name_std, F.text)
async def vvod_name_std_set_name_prepod(message: types.message, state=FSMContext):
    context = {'name_std': F.text}
    doc.render(context)
    await message.answer("Напишите ваше имя преподавателя(Пример: И. И. Иванов)")
    await state.set_state(Decor_tit_List.name_prepod)

@hndl_tit_list_router.message(Decor_tit_List.name_prepod, F.text)
async def vvod_name_prepod_set_degree(message: types.message, state=FSMContext):
    context = {'name_prepod': F.text}
    doc.render(context)
    await message.answer("Напишите начную степень вашего преподавателя (Пример: Кандидат экономических наук)")
    await state.set_state(Decor_tit_List.degree)

@hndl_tit_list_router.message(Decor_tit_List.degree, F.text)
async def vvod_degree_set_zvanie(message: types.message, state=FSMContext):
    context = {'degree': F.text}
    doc.render(context)
    await message.answer("Напишите начное звание вашего преподавателя (Пример: Доцент)")
    await state.set_state(Decor_tit_List.zvanie)

@hndl_tit_list_router.message(Decor_tit_List.zvanie, F.text)
async def vvod_zvanie(message: types.message, state=FSMContext):
    context = {'zvanie': F.text}
    doc.render(context)
    await message.answer("Ваш титульный лист готов!", reply_markup=kbd.tit_list_kb)
    await state.clear()

@hndl_tit_list_router.message(F.text.lower() == 'получить файл')
async def file_docx_tit_list(message: types.message):
    context = {'year': today.year}
    doc.render(context)
    doc.save("tit_list.docx")
    await message.answer_document(types.FSInputFile(r'C:\Users\koles\PycharmProjects\bot\TelegramBot\tit_list.docx'))
    os.remove("tit_list.docx")

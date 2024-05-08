import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart, and_f
from aiogram.utils.markdown import hbold
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

AJ = "6893560935:AAEVWrLZ0FufBNtkVEbLo-6BfwJjMQVB6gE"
ADMIN_ID = 6167775229
logging.basicConfig(level=logging.INFO)
bot = Bot(token=AJ,protect_content=True)
dp = Dispatcher()
user_ids = []
url = "https://javlon6bek.pythonanywhere.com/"


@dp.message(F.text == "🔙 𝗼𝗿𝗾𝗮𝗴𝗮")
async def orqaga(message: types.Message):
    await message.answer(f"Assalomu alaykum,{message.from_user.full_name}")


t = [[types.KeyboardButton(text="📊 𝗦𝘁𝗮𝘁𝗶𝘀𝗸𝗮"), types.KeyboardButton(text="📨 𝗥𝗲𝗸𝗹𝗮𝗺𝗮")],
     [types.KeyboardButton(text="🔍 𝗞𝗶𝗻𝗼 𝗾𝗶𝗱𝗶𝗿𝗶𝘀𝗵"), types.KeyboardButton(text="🎬 𝗞𝗶𝗻𝗼 𝗾𝗼'𝘀𝗵𝗶𝘀𝗵")],
     [types.KeyboardButton(text="🔙 𝗼𝗿𝗾𝗮𝗴𝗮")]
     ]
tugma = types.ReplyKeyboardMarkup(keyboard=t, resize_keyboard=True, )


@dp.message(Command("admin"))
async def admin(message: types.Message):
    id = message.from_user.id
    if id == ADMIN_ID:
        await message.answer("tanlang", reply_markup=tugma)
    else:
        stiker = "CAACAgEAAxkBAAEMD6NmON3FtCrG4V0_VzxeMug-m9YneAACBQMAArAxGUQ-kCLtqQSXiTUE"
        await bot.send_sticker(id, sticker=stiker, reply_markup=inline_tugma2)


# @dp.message(F.text == "🏠 𝗔𝘀𝗼𝘀𝗶𝘆 𝗺𝗲𝗻𝘆𝘂")
# async def admin(message: types.Message):
#     id = message.from_user.id
#     stiker = "CAACAgEAAxkBAAEMD6VmON3SehZUyxMxGVjrm-L03LUH_AACWwMAApMVIUQfKX8I6afbnDUE"
#     await bot.send_sticker(id,sticker=stiker)

@dp.message(F.text == "🔰 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮")
async def admin(message: types.Message):
    id = message.from_user.id
    stiker = "CAACAgEAAxkBAAEMD6NmON3FtCrG4V0_VzxeMug-m9YneAACBQMAArAxGUQ-kCLtqQSXiTUE"
    await bot.send_sticker(id, sticker=stiker)


@dp.message(F.text == "🎬 𝗞𝗶𝗻𝗼 𝗾𝗼'𝘀𝗵𝗶𝘀𝗵")
async def admin(message: types.Message):
    id = message.from_user.id
    if id == ADMIN_ID:
        stiker = "CAACAgEAAxkBAAEMDq1mN5vQewXb91ntcqewlHm77q04HwACXQQAAsjRGETv0HseLYp8LTUE"
        await bot.send_sticker(id, sticker=stiker, reply_markup=inline_tugma3)
    else:
        stiker = "CAACAgEAAxkBAAEMD6NmON3FtCrG4V0_VzxeMug-m9YneAACBQMAArAxGUQ-kCLtqQSXiTUE"
        await bot.send_sticker(id, sticker=stiker, reply_markup=inline_tugma2)


@dp.message(F.text == "🔍 𝗞𝗶𝗻𝗼 𝗾𝗶𝗱𝗶𝗿𝗶𝘀𝗵")
async def admin(message: types.Message):
    id = message.from_user.id
    if id == ADMIN_ID:
        stiker = "CAACAgEAAxkBAAEMEC9mOQ-wHbDqi-8aTDcluy3_3RLaqgACOAIAAk1a2Uaq2G94DeeRnzUE"
        await bot.send_sticker(id, sticker=stiker, reply_markup=inline_tugma3)
    else:
        stiker = "CAACAgEAAxkBAAEMD6NmON3FtCrG4V0_VzxeMug-m9YneAACBQMAArAxGUQ-kCLtqQSXiTUE"
        await bot.send_sticker(id, sticker=stiker, reply_markup=inline_tugma2)


kanal_id = '-1001721160905'
inline_tugma = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="📲 Kanal", url="https://t.me/Ajyuz")],
                     [InlineKeyboardButton(text="✅Obuna bo'ldim", url="https://t.me/AJyUzBot?start=0")]
                     ])

inline_tugma2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="📱𝗞𝗮𝗻𝗮𝗹", url="https://t.me/Ajyuz")],
                     [InlineKeyboardButton(text="🔰 𝗤𝗼'𝗹𝗹𝗮𝗻𝗺𝗮", callback_data="qollanma")],
                     [InlineKeyboardButton(text="👨🏻‍💻 𝗔𝗱𝗺𝗶𝗻", url="https://t.me/javlon6ekbot")]
                     ])

inline_tugma3 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="🎬 𝗞𝗶𝗻𝗼 𝗾𝗼'𝘀𝗵𝗶𝘀𝗵",
                                           url="https://javlon6bek.pythonanywhere.com/admin/kinolar/moviesmodel/")],
                     [InlineKeyboardButton(text="🔍 𝗞𝗶𝗻𝗼 𝗾𝗶𝗱𝗶𝗿𝗶𝘀𝗵", url="http://asilmedia.org/")]
                     ])


@dp.callback_query(F.data == "qollanma")
async def inlinebutton(callback: types.CallbackQuery):
    await callback.answer(
        text=f"📲  Kanalga kirib  📥 Yuklash\n            tugmasini bosing\n\nYoki 🔍Kod yozib yuboring \n    ♻️Kod bu =  biror son",
        show_alert=True)


@dp.callback_query(F.data == "admin")
async def inlinebutton(callback: types.CallbackQuery):
    await callback.answer(text=f"1", show_alert=True)


from aiogram.filters import Filter
from aiogram import Bot
from aiogram.types import Message
import random
from aiogram.utils.chat_action import ChatActionSender
from asyncio import sleep


class CheksupChanel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(kanal_id, message.from_user.id)
        if user_status.status in ['creator', 'administrator', "member"]:
            return False
        return True


@dp.message(CheksupChanel())
async def get_chanel(message: Message):
    odi = message.from_user.full_name
    responses = [f"*{odi}\n🥹 Kanalga obuna boʻling🫶*",
                 f"*{odi}\n👀 Kanalga obuna boʻling🫵*",
                 f"*{odi}\n🤔Kanalga obuna boʻling👇*",
                 f"*{odi}\n😿 Kanalga obuna boʻling*",
                 f"*{odi}\n😇 Kanalga obuna boʻling 🤗*",
                 f"*{odi}\n🙂 Kanalga obuna boʻling*"]
    stickers = ["CAACAgEAAxkBAAEMDqRmN5oN05GMj4kQ2iKXwZ5uoQP5NAACGwIAA9QYRJJGaF1AOkZNNQQ",
                "CAACAgEAAxkBAAEMDqtmN5vElNcwP0sb3f_j-ItL4Qo59QACXQMAAokOMETEAQJ5PWwuZzUE",
                "CAACAgEAAxkBAAEMDq1mN5vQewXb91ntcqewlHm77q04HwACXQQAAsjRGETv0HseLYp8LTUE"]
    response = random.choice(responses)
    sticker_id = random.choice(stickers)

    await bot.send_sticker(message.chat.id, sticker_id)
    await message.reply(text=response, reply_markup=inline_tugma, parse_mode=ParseMode.MARKDOWN_V2)


@dp.message(Command("start"))
async def hastart(message: Message):
    r = requests.get(url).json()
    id = message.from_user.id
    odi = message.from_user.first_name
    stiker = "CAACAgEAAxkBAAEMDmZmN34yqkhpK6s0ropOmkxmqBaLewACkQIAAoW5oUb3wzj1mLg2uTUE"
    tugma = InlineKeyboardBuilder()
    tugma.row(types.InlineKeyboardButton(
        text="📲 Profilni ko'rish", url=f"tg://user?id={id}"))
    if id not in user_ids:
        user_ids.append(id)
        await bot.send_sticker(ADMIN_ID, sticker=stiker)
        await bot.send_message(ADMIN_ID,
                               f"*✅ Yangi Foydanuvchi\n\n👤 Ismi : {odi}\n🆔 IDsi : __{id}__\n🤖 Jami: {len(user_ids)} Ta foydalanuvchi*",
                               reply_markup=tugma.as_markup(), parse_mode=ParseMode.MARKDOWN_V2, )
    else:
        await bot.send_message(ADMIN_ID, f"{odi} \n♻️ Botga /start berdi\n\n🤖 Jami: {len(user_ids)} Ta foydalanuvchi")

    start_param = message.text.split(' ')[-1]
    for i in r:
        try:
            if int(start_param) == int(i['kod']):
                async with ChatActionSender.upload_video(message.from_user.id, bot):
                    await sleep(2)
                    await message.answer_video(video=i['silka'], caption=i['qoshimcha'])

        except ValueError:

            odi = message.from_user.full_name
            responses = [f"*Assalomu aleykum 😇\n{odi}\n\n🤖Botni ishlatishdan oldin\n__🔰Qoʻllanmani koʻring__ 🤔*",
                         f"*Assalomu aleykum {odi}\nKanalga kirib __📥Yuklash__\n  tugmasini bosing*",
                         f"*Assalomu aleykum {odi}\n    🤔 Kod yozing\n\n__👇Kodlar Kanalda bor__*"]

            stickers = "CAACAgEAAxkBAAEMDpRmN5EU3__BYK6pAAEgBgqO-PLW8gkAAqUCAAJG_vBHOOuwXycUPHY1BA"
            await bot.send_sticker(message.chat.id, stickers)
            response = random.choice(responses)
            await message.reply(text=response, reply_markup=inline_tugma2, parse_mode=ParseMode.MARKDOWN_V2)
            break


m1 = []
m2 = []


@dp.message(F.text == "📨 𝗥𝗲𝗸𝗹𝗮𝗺𝗮")
async def cmd_reklama(message: Message):
    st = ["CAACAgEAAxkBAAEMD7dmON_ncFrWDtKguT7NIV90gH7rEwACvQIAAhAkWURYtO2ITIqP2jUE",
          "CAACAgEAAxkBAAEMD7NmON-OSOrbHTajYdPkL6S4Xu10AQACIgMAAma-oUY566OY856vSzUE",
          "CAACAgEAAxkBAAEMD5tmON2ZPMyp0LOtxKWxWlBRapDcpAAC1gIAAsJmoEarz8M8Ok2fmTUE"]

    if message.from_user.id == ADMIN_ID:
        if message.reply_to_message:
            for user_id in user_ids:
                try:

                    if message.reply_to_message.content_type in ['photo', 'video', 'audio', 'document']:
                        await bot.copy_message(
                            chat_id=user_id,
                            from_chat_id=message.chat.id,
                            message_id=message.reply_to_message.message_id
                        )
                    else:
                        await bot.send_message(
                            chat_id=user_id,
                            text=message.reply_to_message.text
                        )
                    m1.append(1)
                except Exception as e:

                    m2.append(1)
                    await message.reply(f"😢Foydalanuvchi {user_id} botni bloklagan")

            st = ["CAACAgEAAxkBAAEMD51mON2nMjqP1L5yRksWUC2nnA3wzgAC2AIAAox2IUSzVy31WuqdqDUE",
                  "CAACAgEAAxkBAAEMD59mON2x5JMoivKMGxGZCLCEAW-OXgACnwMAAonfWETOikC8ytx7RTUE",
                  "CAACAgEAAxkBAAEMD7lmOOE3F58FOFxIGptjvboXziWotgACegMAAlpTMEQuAAF6_RO-Apw1BA"]
            stiker = random.choice(st)
            await message.answer_sticker(sticker=stiker)
            await message.answer(f"✅ {len(m1)} Muvaffaqiyatli\n ❌{len(m2)} Muvaffaqiyatsiz")


        else:
            stiker = random.choice(st)
            await bot.send_sticker(ADMIN_ID, sticker=stiker)
            await message.reply("Tarqatmoqchi bo'lgan xabaringizga reply qiling")
    else:
        await message.reply("Siz admin emassiz!")


@dp.message(F.text == "📊 𝗦𝘁𝗮𝘁𝗶𝘀𝗸𝗮")
async def admin(message: types.Message):
    id = message.from_user.id
    stiker = "CAACAgEAAxkBAAEMD_tmOQABZJc7bB_TuCcTeBRDKMMvFUQAAooCAAKRSSBEFaWpiC-NrAo1BA"
    await bot.send_sticker(id, sticker=stiker)
    await message.answer(
        f"📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝗶𝘀𝗸𝗮\n👾 @AJyUzBot\n\n\n✅  𝗙𝗮𝗼𝗹 - {len(m1)}\n❌ 𝗡𝗼𝗳𝗮𝗼𝗹 - {len(m2)}\n👥 𝗝𝗮𝗺𝗶  - {len(user_ids)}\n\n\n⚙ 𝗬𝗮𝗿𝗮𝘁𝗶𝗹𝗱𝗶 8.05.2024")


@dp.message(F.text.isdigit())
async def kino(message: types.Message):
    r = requests.get(url).json()
    for i in r:
        if int(message.text) == int(i['kod']):
            async with ChatActionSender.upload_video(message.from_user.id, bot):
                await bot.send_sticker(message.from_user.id,
                                       sticker="CAACAgEAAxkBAAEMDtdmN860jf2dHnPGmTkdaz8Wd9X7HgACLQIAAqcjIUQ9QDDJ7YO0tjUE")

                await sleep(2)
                await message.answer_video(video=i['silka'], caption=i['qoshimcha'])


@dp.message(F.text)
async def kino(message: types.Message):
    async with ChatActionSender.typing(message.from_user.id, bot):
        responses = [f"*Kanalga kirib 📥Yuklash \ntugmasini bosing*",
                     f"*🤔 Kod yozing\n\n__👇Kodlar Kanalda bor__*",
                     f"*👀 Agar siz 🔍qidirgan kino\nbizni botda boʻlmasa ♻️\n\n⚜Adminga yozing va\nKino 📝 Buyurtma qiling*"]
        await sleep(2)
        response = random.choice(responses)
        await message.reply(text=response, reply_markup=inline_tugma2, parse_mode=ParseMode.MARKDOWN_V2)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

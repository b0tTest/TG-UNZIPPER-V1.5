# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
class Buttons:
    START_BUTTON=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("๐ค Creator", url="https://telegram.me/OO7ROBOT"),
                InlineKeyboardButton("๐ค OtherBotZ", url="https://telegram.me/mybotzlist")
            ],[
                InlineKeyboardButton("โ๏ธ Help", callback_data="helpcallback"),
                InlineKeyboardButton("๐ About", callback_data="aboutcallback"),
                InlineKeyboardButton("โ Cancel", callback_data="close")
            ]
        ]
    )
    
    CHOOSE_E_BTN=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("File Extract ๐", callback_data="extract_file|tg_file|no_pass"),
                InlineKeyboardButton("File (Password) Extract ๐", callback_data="extract_file|tg_file|with_pass")
            ],
            [
                InlineKeyboardButton("๐ Url Extract ๐", callback_data="extract_file|url|no_pass"),
                InlineKeyboardButton("๐ (Password) Url Extract ๐", callback_data="extract_file|url|with_pass")
            ],
            [
                InlineKeyboardButton("โ Cancel ๐", callback_data="cancel_dis")
            ]
        ]
    )

    CLN_BTNS=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Clean My Files ๐", callback_data="cancel_dis")
            ],
            [
                InlineKeyboardButton("TF! Nooo ๐ณ", callback_data="nobully")
            ]
        ]
    )
    
    ME_GOIN_HOME=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Back to Home ๐ก", callback_data="megoinhome")
            ]
        ]
    )




class Messages:
    START_TEXT = """
Hi ๐ **{}**,
__a Simple  Telegram__ **Unzipper Bot**๐ณ๏ธ\n__to Extract Various Types Of Archive like rar, zip, tar, 7z, tar.xz etc..__
ยป __Support Archive Url Link too__

**Made with โค๏ธ by @MyTestBotZ**
    """

    HELP_TXT = """
**How To Extract? ๐ค๐ค๐ค**

__1. Send the File or Link that you want to Extract.
2. Click on extract button
      (If you sent a link use "Url Extract" button. If it's a File just use "File Extract" button).
3. wait for starting the Process..__

**Note:**
    **1.** __If your archive is password protected select__ **(Password) Extract๐ณ๏ธ** __mode. Bot isn't a GOD to know your file's password so If this happens just send that password!__
    
    **2.** __Please don't send corrupted files! If you sent a one by a mistake just send__ ** /clean** __command!__
    """

    ABOUT_TXT = """
**@TG_UnzipperBot**
โช ยป **Creator :** [Meeeee...](https://telegram.me/OO7ROBot)
โช ยป **Channel:** [MyTestBotZ](https://telegram.me/MyTestBotZ)
โช ยป **Other Bots:** [Other BotZ](https://telegram.me/mybotzlist)
โช ยป **Language:** [Python](https://www.python.org/)
โช ยป **Framework:** [Pyrogram](https://docs.pyrogram.org/)
โช ยป **Dev: Itz-fork**
โช ยป **Build Version: V1**
    """

    LOG_TXT = """
**Extract Log ๐!**
**User ID:** `{}`
**File Name:** `{}`
**File Size:** `{}`
    """

    AFTER_OK_DL_TXT = """
**โ Successfully Downloaded ๐ฅ**

**Download time:** `{}`
**Status:** `Trying to extract the archive`

**ยฉ @TG_UnZipperbot**
    """

    EXT_OK_TXT = """
**โ๏ธ Extraction Successfull! ๐๐**
**Extraction time:** `{}`
**Status:** `Trying to upload ๐ค`
    """

    EXT_FAILED_TXT = """
**Extraction Failed ๐!**
**What to do?**
 - Please make sure archive isn't corrupted
 - Please make sure that you selected the right mode!
 - May be Your archive format isn't supported ๐
    """

    ERROR_TXT = """
**Error Happend ๐!**
**ERROR:** {}
    """

    CANCELLED_TXT = """
**{} โ!**
`Now all of your files have been deleted from my server ๐!`
    """

    CLEAN_TXT = """
**Are sure want to delete your files from my server ๐ค?**
**Note:** `This action cannot be undone!`
    """

# List of error messages from p7zip
ERROR_MSGS = [
    "Error",
    "Can't open as archive"
    ]

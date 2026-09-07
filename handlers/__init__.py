from aiogram import Dispatcher

from .start import register_start_handlers, register_beer_handlers

def register_all_handlers(dp: Dispatcher):
    
    register_start_handlers(dp)
    register_beer_handlers(dp)

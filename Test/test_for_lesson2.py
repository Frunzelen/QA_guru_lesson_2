
import pytest
from selene.support.shared import browser
from selene import be, have

def test_for_search_string_true():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    print('В выдаче браузера есть результаты поиска')

def test_for_search_string_false():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('567кен8/*').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу 567кен8/* ничего не найдено'))
    print('В выдаче браузера нет результатов поиска')
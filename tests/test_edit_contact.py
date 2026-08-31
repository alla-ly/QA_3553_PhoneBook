from faker import Faker
from data.contact_data import create_contact
from pages.add_new_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()


def test_edit_contact_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_name = fake.first_name()
    contact_page.fill_name(new_name)
    contact_page.click_save_btn()

    assert contact_page.get_contact_name_value() == new_name


def test_edit_contact_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_last_name = fake.last_name()
    contact_page.fill_last_name(new_last_name)
    contact_page.click_save_btn()

    assert contact_page.get_contact_last_name_value() == new_last_name


def test_edit_contact_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_phone_number = fake.phone_number()
    contact_page.fill_phone(new_phone_number)
    contact_page.click_save_btn()

    assert contact_page.get_contact_phone_value() == new_phone_number


def test_edit_contact_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_email = fake.email()
    contact_page.fill_email(new_email)
    contact_page.click_save_btn()

    assert contact_page.get_contact_email_value() == new_email


def test_edit_contact_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_address = fake.address()
    contact_page.fill_address(new_address)
    contact_page.click_save_btn()

    assert contact_page.get_contact_address_value() == new_address


def test_edit_contact_description(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    test_contact = create_contact()
    contact_page.open_contact_form()
    contact_page.fill_contact_form(test_contact)
    contact_page.submit_contact()

    contacts_page.open_contact_details(test_contact.phone)

    contact_page.click_edit_button()
    new_description = "Updated contact description"
    contact_page.fill_desc(new_description)
    contact_page.click_save_btn()

    assert contact_page.get_contact_description_value() == new_description




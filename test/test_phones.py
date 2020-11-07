import re

def test_phones_on_homepage(app):
    contact_homepage = app.contact.get_contact_list()[0]
    contact_edit_homepage = app.contact.get_contact_info_from_editpage(0)
    assert contact_homepage.all_phones_from_homepage == merge_phones(contact_edit_homepage)

def test_phones_on_viewpage(app):
    contact_viewpage = app.contact.get_contact_from_viewpage(0)
    contact_edit_homepage = app.contact.get_contact_info_from_editpage(0)
    assert contact_viewpage.homephone == contact_edit_homepage.homephone
    assert contact_viewpage.mobilephone == contact_edit_homepage.mobilephone
    assert contact_viewpage.workphone == contact_edit_homepage.workphone
    assert contact_viewpage.secondaryphone == contact_edit_homepage.secondaryphone

def clear(string):
    return re.sub("[() -]","",string)

def merge_phones(contact):
    # Применим функицию map ко всему списку, можно было записать отдельно каждый (clear(contact.homephone) и т.д.)
    return "\n".join(filter(lambda x:x!="",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.homephone,contact.workphone,contact.mobilephone,contact.secondaryphone]))))
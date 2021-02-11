from fastapi import Header


x_version_header = Header(None, title="Current API version", alias="X-Version")
x_lang_header = Header(None, title="Current localization", alias="X-Lang")

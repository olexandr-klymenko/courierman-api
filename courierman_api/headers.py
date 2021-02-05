from fastapi import Header


x_version_header = Header(None, title="Current API version", alias="X-Version")

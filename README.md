# 📝 font-service
A Flask wrapper arround Fonttools. Everyone that ever worked with subsetting knows the pain. Fonttools seems to be the best tool to work with subsetting. This service can convert  OTF and TTF to WOFF/TTF and subest fonts


## subset
send a base64 TTF font and a subset text
endpoint: `/subset`
```json
{
    "text": "this is a text that needs to be subsetted",
    "font": "data:;base64,AAEAAAATAQAABAAwRFNJR54SRB0AAzucAAAVdEdERUYAJgOvAAM3fAAAAB5HUE9TCzcPNwADN5wAAAA4R1NVQg4rPbcAAzfUAAADxk9TLzKhPp7JAAABuAAAAGBjbWFwKasvaAAAELQAAAQaY3Z0IA9NGKQAAB2QAAAAomZwZ21+a+VF2k6RQPCf7zsfJ0pWrDr9qJRqfPecwX97k2BOG8QrV5WUyxbhmmcz0SspE8jsvrxZsQOkKZnsHYiZJId3D5vKFPvU1ElMdA7IPS5vIMkDzejlD9AhObNWGdX7rL2sqTi9sNUMo9ljrbCVtGhYw+LXKf+RpMcAAA=="
}
```

## converting 
Send a font in base64 and the type. The service will return a base64 of TTF and WOFF 
endpoint: `/convert`
```json
{
    "type": "otf",
    "font": "data:;base64,AAEAAAATAQAABAAwRFNJR54SRB0AAzucAAAVdEdERUYAJgOvAAM3fAAAAB5HUE9TCzcPNwADN5wAAAA4R1NVQg4rPbcAAzfUAAADxk9TLzKhPp7JAAABuAAAAGBjbWFwKasvaAAAELQAAAQaY3Z0IA9NGKQAAB2QAAAAomZwZ21+a+VF2k6RQPCf7zsfJ0pWrDr9qJRqfPecwX97k2BOG8QrV5WUyxbhmmcz0SspE8jsvrxZsQOkKZnsHYiZJId3D5vKFPvU1ElMdA7IPS5vIMkDzejlD9AhObNWGdX7rL2sqTi9sNUMo9ljrbCVtGhYw+LXKf+RpMcAAA=="
}
```

logging is done with logentries, you can rename the `settings.example.ini` to `settings.ini` and have your logging sent to logentries.

```
[logentries]
key=your_key
```

I included a Dockerfile which is very basic, make sure you change the exposed ports if you want to run on another port. 
```bash
FROM python:2

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9097

CMD [ "python", "app.py" ]
```

import cv2
import pytesseract
import re
import spacy

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    processed_image = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    return processed_image


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text


def extract_email(text):
    email_pattern = r"\S+@\S+"
    email = re.findall(email_pattern, text)
    return email


def extract_phone(text):
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    phone = re.findall(phone_pattern, text)
    return phone


def extract_company(text):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)
    # Extract names
    return [ent.text for ent in doc.ents if ent.label_ == "ORG"]


def extract_names(text):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_md")
    doc = nlp(text)
    # Extract names
    return [ent.text for ent in doc.ents if ent.label_ == "PERSON"]

def ocr_extract(image):
    processed_image = preprocess_image(image)
    text = extract_text_from_image(processed_image)
    names = extract_names(text)
    emails = extract_email(text)
    phones = extract_phone(text)
    company = extract_company(text)

    print(f"Extracted names: {names}")
    print(f"Extracted emails: {emails}")
    print(f"Extracted phones: {phones}")
    print(f"Extracted company: {company}")

    return [company, names, emails, phones]

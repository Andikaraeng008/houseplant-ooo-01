import os

TEXT = "I am out of office until someone waters me. My last drink was in March. Please send sunlight, not meetings."

def main():
    assert 1 <= len(TEXT) <= 120 and TEXT.strip(), "gate: 1-120 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

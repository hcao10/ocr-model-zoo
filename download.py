import hashlib
import os
import sys
import urllib.request

MODELS = {
    "fast_tiny_fp16": {
        "url": "https://github.com/hcao10/ocr-model-zoo/releases/download/v0.1.0/fast_tiny_fp16.onnx",
        "sha256": "e96445ff31f6d6dce481743df441f9675b25e93697b06470583a46ebd77382e7",
    },
    "crnn_mobilenet_v3_small_fp16": {
        "url": "https://github.com/hcao10/ocr-model-zoo/releases/download/v0.1.0/crnn_mobilenet_v3_small_fp16.onnx",
        "sha256": "8f1bccd294027b7ca8bd85f05152e9676046487947a5068f5d9681a60b54e8d4",
    },
}


def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def download_model(name, output_dir="."):
    if name not in MODELS:
        print(f"[ERROR] Model '{name}' not found in registry.")
        print("Available models:", ", ".join(MODELS.keys()))
        sys.exit(1)

    info = MODELS[name]
    url = info["url"]
    sha256 = info["sha256"]
    file_path = os.path.join(output_dir, f"{name}.onnx")

    # Download
    print(f"Downloading {name} from {url}")
    urllib.request.urlretrieve(url, file_path)

    # Verify checksum
    print("Verifying SHA256...")
    checksum = sha256sum(file_path)
    if checksum != sha256:
        print(f"[ERROR] SHA256 mismatch for {name}!")
        print(f"Expected: {sha256}")
        print(f"Got:      {checksum}")
        os.remove(file_path)
        sys.exit(1)

    print(f"Model '{name}' downloaded and verified successfully: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download.py <model_name> [output_dir]")
        print("Available models:", ", ".join(MODELS.keys()))
        sys.exit(1)

    model_name = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(output_dir, exist_ok=True)

    download_model(model_name, output_dir)

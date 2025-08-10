# OCR Model Zoo

A collection of ONNX models for Optical Character Recognition (OCR), optimized for various precisions  
(FP32, FP16, INT8) and GPU/CPU deployment.

---

## Available Models

### fast_tiny_fp16.onnx

- **Precision**: FP16 (GPU only)
- **SHA256**: `e96445ff31f6d6dce481743df441f9675b25e93697b06470583a46ebd77382e7`
- **Input shape**: `(1, 3, 1024, 1024)`
- **Mean difference from FP32**: `0.1930888742`
- **Performance**:
  - 40.05 ms ± 0.35 ms (FP16)

### crnn_mobilenet_v3_small_fp16.onnx

- **Precision**: FP16 (GPU only)
- **SHA256**: `8f1bccd294027b7ca8bd85f05152e9676046487947a5068f5d9681a60b54e8d4`
- **Input shape**: `(1, 3, 32, 128)`
- **Mean difference from FP32**: `0.0134673705`
- **Performance**:
  - 3.86 ms ± 0.06 ms (FP16)

---

## Download

Models are hosted in the [Releases](../../releases) section.

Example:

```bash
wget https://github.com/hcao10/ocr-model-zoo/releases/download/v0.1.0/fast_tiny_fp16.onnx
wget https://github.com/hcao10/ocr-model-zoo/releases/download/v0.1.0/crnn_mobilenet_v3_small_fp16.onnx
```

---

## Verify Integrity

```bash
sha256sum fast_tiny_fp16.onnx
sha256sum crnn_mobilenet_v3_small_fp16.onnx
```

---

## License

MIT License

````

---

### 3. LICENSE（MIT）
```text
MIT License

Copyright (c) 2025 hcao10

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
````

from pathlib import Path
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

ROOT = Path(__file__).parent

ext_modules = [
    CppExtension(
        name="metal_flash_attn",
        sources=[
            "src/metal_flash_attention.mm",
            "src/metal_binding.cpp",
        ],
        include_dirs=[
            "src",
        ],
        language="c++",
        extra_compile_args=[
            "-std=c++17",
            "-fPIC",
            "-Wall",
            "-O3",
        ],
        extra_link_args=[
            "-framework", "Metal",
            "-framework", "Foundation",
        ],
    )
]

long_description = ""
readme = ROOT / "README.md"
if readme.exists():
    long_description = readme.read_text(encoding="utf-8")

setup(
    name="metal-flash-attention",
    version="1.0.0",
    description="Metal-accelerated FlashAttention for PyTorch on Apple Silicon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Metal FlashAttention Contributors",
    python_requires=">=3.10",
    install_requires=[
        "torch>=2.0.0",
    ],
    packages=["metal_flash_attention"],
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension.with_options(use_ninja=False)},
    zip_safe=False,
)

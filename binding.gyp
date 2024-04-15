{
  "targets": [
    {
      "target_name": "hdiffpatch",
      "sources": [
        "src/main.cc",
        "src/hdiff.cpp",
        "HDiffPatch/libHDiffPatch/HPatch/patch.c",
        "HDiffPatch/libHDiffPatch/HDiff/diff.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/bytes_rle.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/suffix_string.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/compress_detect.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/libdivsufsort/divsufsort64.c",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/libdivsufsort/divsufsort.c",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/limit_mem_diff/digest_matcher.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/limit_mem_diff/stream_serialize.cpp",
        "HDiffPatch/libHDiffPatch/HDiff/private_diff/limit_mem_diff/adler_roll.c",
        "lzma/C/LzFind.c",
        "lzma/C/LzmaDec.c",
        "lzma/C/LzmaEnc.c",
        "lzma/C/Lzma2Dec.c",
        "lzma/C/Lzma2Enc.c"
      ],
      "defines": [
        "_IS_NEED_DIR_DIFF_PATCH=0",
        "_7ZIP_ST",
        "_IS_USED_MULTITHREAD=0"
      ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
    }
  ]
}

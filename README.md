# Tobu Tobu Girl Deluxe ![MIT License](https://img.shields.io/badge/license-MIT%20License-blue.svg) ![CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg) ![Game Boy](https://img.shields.io/badge/platform-Game%20Boy-blue.svg)

A dual GB/GBC remaster of Tobu Tobu Girl.

More info at: http://tangramgames.dk/tobutobugirldx.

This fork changes the code so that it can be built with just GBDK-2020, greatly simplifying the build process.

## Playing the game

In order to play the game you will need to either flash the game to a Game Boy flash cart or use a Game Boy emulator. The binaries are provided through [itch.io](https://tangramgames.itch.io/tobutobugirldx).

## Compilation
This fork eliminates the need for different versions of GBDK and SDCC, so only GBDK-2020 is required. pyimgtogb is also included in the repository.

* [GBDK-2020](https://github.com/gbdk-2020/gbdk-2020)
* [mmlgb](https://github.com/SimonLarsen/mmlgb)

### config.mk 사용 방법

빌드 시 GBDK-2020의 경로를 커스터마이징하려면 프로젝트 루트에 `config.mk` 파일을 생성하고 다음 내용을 추가하세요:

```makefile
GBDKDIR = /path/to/your/gbdk
```

`config.mk` 파일이 없으면 기본값으로 `./gbdk` 경로를 사용합니다.

## License

The source code for Tobu Tobu Girl is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

All assets (images, text, sound and music) are licensed under the [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

#!/usr/bin/env python3
"""
PNG 파일을 indexed color PNG로 변환하는 스크립트
"""
import argparse
import sys
from PIL import Image

def convert_to_indexed(input_path, output_path, colors=256, dither='NONE'):
    """
    PNG 파일을 indexed color로 변환
    
    Args:
        input_path: 입력 PNG 파일 경로
        output_path: 출력 PNG 파일 경로
        colors: 팔레트 색상 수 (기본값: 256)
        dither: 디더링 방법 ('NONE', 'FLOYDSTEINBERG', 'ORDERED')
    """
    try:
        # 이미지 로드
        img = Image.open(input_path)
        
        # 이미지가 이미 indexed color인 경우 확인
        if img.mode == 'P':
            print(f"이미지가 이미 indexed color 모드입니다.")
            img.save(output_path)
            return
        
        # RGB/RGBA로 변환 (필요한 경우)
        if img.mode not in ('RGB', 'RGBA'):
            img = img.convert('RGB')
        
        # 디더링 옵션 설정
        dither_map = {
            'NONE': Image.Dither.NONE,
            'FLOYDSTEINBERG': Image.Dither.FLOYDSTEINBERG,
            'ORDERED': Image.Dither.ORDERED
        }
        dither_mode = dither_map.get(dither.upper(), Image.Dither.NONE)
        
        # Indexed color로 변환
        if img.mode == 'RGBA':
            # 투명도가 있는 경우
            # 먼저 RGB로 변환하고, 투명도를 마스크로 처리
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[3])  # alpha 채널을 마스크로 사용
            indexed_img = rgb_img.quantize(colors=colors, dither=dither_mode)
        else:
            indexed_img = img.quantize(colors=colors, dither=dither_mode)
        
        # 저장
        indexed_img.save(output_path)
        print(f"변환 완료: {input_path} -> {output_path}")
        print(f"팔레트 색상 수: {len(indexed_img.getcolors())}")
        
    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다: {input_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"오류: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='PNG 파일을 indexed color PNG로 변환',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예제:
  %(prog)s input.png output.png
  %(prog)s input.png output.png --colors 16
  %(prog)s input.png output.png --colors 4 --dither FLOYDSTEINBERG
        """
    )
    parser.add_argument('input', help='입력 PNG 파일 경로')
    parser.add_argument('output', help='출력 PNG 파일 경로')
    parser.add_argument(
        '--colors', 
        type=int, 
        default=256,
        help='팔레트 색상 수 (기본값: 256, Game Boy는 보통 4)'
    )
    parser.add_argument(
        '--dither',
        choices=['NONE', 'FLOYDSTEINBERG', 'ORDERED'],
        default='NONE',
        help='디더링 방법 (기본값: NONE)'
    )
    
    args = parser.parse_args()
    
    convert_to_indexed(args.input, args.output, args.colors, args.dither)

if __name__ == '__main__':
    main()

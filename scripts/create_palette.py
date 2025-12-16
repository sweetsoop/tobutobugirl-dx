#!/usr/bin/env python3
"""
JSON 파일에서 색상 팔레트를 읽어서 팔레트 이미지를 생성하는 스크립트
각 색상을 1x1 픽셀로 만들어 가로로 나열합니다.
"""

import json
import sys
from PIL import Image


def hex_to_rgb(hex_color):
    """16진수 색상 코드를 RGB 튜플로 변환"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def create_palette_image(json_path, output_path=None):
    """
    JSON 파일에서 색상 팔레트를 읽어서 이미지로 생성
    
    Args:
        json_path: JSON 파일 경로
        output_path: 출력 이미지 경로 (None이면 JSON 파일명 기반으로 생성)
    """
    # JSON 파일 읽기
    with open(json_path, 'r') as f:
        colors = json.load(f)
    
    # 색상 개수 확인
    num_colors = len(colors)
    if num_colors == 0:
        print("경고: 색상이 없습니다.")
        return
    
    # 출력 경로 설정
    if output_path is None:
        output_path = json_path.replace('.json', '.png')
    
    # 이미지 생성: 각 색상을 1x1 픽셀로 가로로 나열
    # 이미지 크기: (색상 개수) x 1
    img = Image.new('RGB', (num_colors, 1))
    
    # 각 색상을 픽셀로 설정
    for i, hex_color in enumerate(colors):
        rgb = hex_to_rgb(hex_color)
        img.putpixel((i, 0), rgb)
    
    # 이미지 저장
    img.save(output_path)
    print(f"팔레트 이미지 생성 완료: {output_path}")
    print(f"이미지 크기: {num_colors}x1 픽셀")
    print(f"색상 개수: {num_colors}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("사용법: python create_palette.py <json_file> [output_file]")
        sys.exit(1)
    
    json_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    create_palette_image(json_path, output_path)

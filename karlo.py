# REST API 호출, 이미지 파일 처리에 필요한 라이브러리
import requests
import json
import urllib
from PIL import Image

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
from secret import KAKAO_REST_API_KEY

# 이미지 생성하기 요청
def t2i(prompt, negative_prompt):
    body = {
        'prompt': prompt,
        'negative_prompt': negative_prompt
    }
    headers = {
        'Authorization': f'KakaoAK {KAKAO_REST_API_KEY}',
        'Content-Type': 'application/json'
    }
    print("\n===== kakao API request =====")
    print(headers)
    print(body)
    r = requests.post(
        'https://api.kakaobrain.com/v2/inference/karlo/t2i',
        json = body,
        headers = headers
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    print("\n===== kakao API response =====")
    print(response)
    print("\n")
    return response


def test():
    # 프롬프트에 사용할 제시어
    # prompt = "A sit cat with white fur, hand drawing, black two eyes, pink nose, white tail, grass background"  # hand drawing, four legs, whiskers on cheek, isometric pixelart, 1px dark natural color outline, 
    # negative_prompt = "dog, human, ugly face, cropped, two or more tails, short tail, front"
    prompt = "luxury fashion look book image, indoors, high resolution photo, detailed object texture, depth of field, cinematic lighting, professional lighting, dramatic shadow, detailed shadow"
    negative_prompt = "comic, cartoon"

    # 이미지 생성하기 REST API 호출
    response = t2i(prompt, negative_prompt)

    # 응답의 첫 번째 이미지 생성 결과 출력하기
    result = Image.open(urllib.request.urlopen(response.get("images")[0].get("image")))
    result.show()

if __name__ == '__main__':
    test()

"""
prompt
(Nikon_RAW_photo, Fujifilm_XT3), (best_quality:1.4, masterpiece), (ultra_highres:1.1, ultra_color), (realistic, photo-realistic:1.2), (shart_focus, intricate_details:1.2), a full-length portrait, 1 woman, solo, body, looking_at_viewer:1.2, detailed_hair, detailed_face, realistic_eyes, detailed_skin_texture, detailed_clothes_texture, luxury fashion look book image, high resolution photo, detailed object texture, depth of field, cinematic lighting, professional lighting, dramatic shadow, detailed shadow

negative prompt
(worst_quality, low_quality:1.4), (lowers:1.1, blurry:1.2, grayscale, monochrome:1.2), ((ng_deepnegative_v1_75t:1.5)), ((badhandv4:1.4)), (bad_proportions:1.3,bad_composition), big_head, big_face, wide_forehead, narrow_shoulders, short_legs
"""
# 데이터로 진단하는 업무지구의 성공과 실패

본 시스템은 가천대학교 스마트시티학과 「스마트시티의 이론과 실제」 기말 대체 제출용 정적 비교분석 시스템이다. 

## 기본 원칙

- 대상지는 사용자가 직접 작성한 polygon 기준이다.
- 면적은 Turf.js로 `pangyo_boundary.geojson`, `cheongna_boundary.geojson`에서 직접 계산한다.
- 건축물, 도로, 버스정류장, 용도지역, 지하철 노드와 등시간권은 현재 polygon 기준으로 다시 계산해 표시한다.
- 그래프는 단위 차이를 줄이기 위해 정규화 지수로 표시한다.
- 실제 수치는 화면의 비교표에서 함께 확인할 수 있다.
- 버스정류장 지표는 보조 대중교통 접근성 지표이다.
- 용도지역도는 실제 GeoJSON 파일이 있을 때만 표시한다.
- 데이터 미확보 항목은 임의로 채우지 않는다.
- 실제 데이터가 없는 출퇴근 시간대 분석과 시뮬레이션 지표는 제외하였다.

## 현재 반영 파일

- `data/metrics.json`
- `data/pangyo_boundary.geojson`
- `data/cheongna_boundary.geojson`
- `data/pangyo_landuse_features.geojson`
- `data/cheongna_landuse_features.geojson`
- `data/pangyo_map_buildings.geojson`
- `data/cheongna_map_buildings.geojson`
- `data/pangyo_map_roads.geojson`
- `data/cheongna_map_roads.geojson`
- `data/bus_stops.geojson`
- `data/pangyo_subway_nodes_60.geojson`
- `data/cheongna_subway_nodes_60.geojson`
- `data/pangyo_subway_accessibility_curve.json`
- `data/cheongna_subway_accessibility_curve.json`
  


## 화면 구성

- 상단 사용자 정보
- 판교/청라 비교 지도
- 지도 바로 위 compact 체크박스 필터
- 건축물 주용도 컬러맵
- 용도지역도 레이어
- 버스정류장 레이어
- 지하철 노드와 등시간권 슬라이더
- 핵심 지표 카드
- 실제 수치 비교표
- 정규화 비교 그래프
- 비교 해석 문단

## 주의

- 총인구, 총가구수, 총종사자수, 총사업체수, 직주비는 현재 제출본의 `metrics.json` 입력값을 사용한다.
- 경계 면적, 용도지역 구성, LUM, 건축물 수, 도로 밀도, 버스정류장 수와 밀도, 등시간권 노드와 접근성은 현재 polygon 기준으로 다시 계산한다.
- `Unexpected token '<'` 오류를 막기 위해 모든 JSON/GeoJSON은 `response.ok` 확인 후 파싱한다.

## 사용 자료 및 출처

- 사용자 정의 boundary polygon
  - `data/pangyo_boundary.geojson`, `data/cheongna_boundary.geojson`
  - 연구자 직접 작성
  - 분석 범위 설정, 지도 시각화, 면적 계산, 자료 clip 기준에 사용

- SGIS 집계구 통계
  - 통계청 SGIS 통계지리정보서비스
  - 총인구, 총가구수, 총종사자수, 총사업체수, 직주비 비교에 사용
  - 집계구와 연구 경계가 완전히 일치하지 않을 수 있어 배분 추정값으로 해석해야 한다.

- VWorld / KLIP 토지이용계획정보
  - 용도지역도, 용도지역 구성비, 토지이용 혼합도(LUM) 산출에 사용
  - 현재 제출본에서는 `data/pangyo_landuse_features.geojson`, `data/cheongna_landuse_features.geojson`을 반영한다.

- 건축HUB 건축물대장
  - 국토교통부 건축HUB
  - 원자료 예시: `pangyo_building_basic_2023.csv`, `cheongna_building_basic_2023.csv`
  - 현재 제출본에서는 건축물 클릭 속성 보조 출처로 참고하며, 실제 연면적·용적률 원필드는 포함하지 않았다.

- 국토지리정보원 수치지도
  - 국토지리정보원 국토정보플랫폼
  - 전처리된 도로·건축물 GeoJSON을 통해 도로망, 건축물 공간자료, 도로 밀도 계산에 사용

- `subway_network.zip`
  - 수업 제공 자료 또는 과제 제공 네트워크 자료
  - 등시간권, 도달 노드 수, 접근성 곡선, 도달 가능 인구·종사자 비교에 사용
  - 현재 제출본에서는 `pangyo_subway_nodes_60.geojson`, `cheongna_subway_nodes_60.geojson`, 각 접근성 curve JSON을 반영한다.

- 국토교통부 버스정류장 위치정보
  - 버스정류장 수와 밀도 산출에 사용
  - 보조 대중교통 접근성 지표이며 핵심 성공 판단 지표는 아니다.

- OpenStreetMap
  - Leaflet 배경지도에 사용
  - 분석 수치 산출용이 아니라 위치 확인용 배경지도다.

- Leaflet / Chart.js / Turf.js
  - 각 공식 CDN 사용
  - Leaflet은 지도 시각화, Chart.js는 그래프 작성, Turf.js는 polygon 면적 계산에 사용

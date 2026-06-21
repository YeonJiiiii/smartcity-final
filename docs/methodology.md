# 분석 방법 개요

## 1. 분석 범위

- 시간범위: 기본 비교연도는 2023년이다.
- 시간단위: 시계열이 아닌 단면 분석이다.
- 공간범위: `data/pangyo_boundary.geojson`, `data/cheongna_boundary.geojson`에 저장된 사용자 정의 업무지구 경계이다.
- 공간단위: 경계 polygon, 집계구, 건축물, 철도역 노드 등 데이터별 단위를 분리하여 기록한다.

## 2. 제2판교 제외 이유

본 제출본의 기본 분석 대상은 제1판교테크노밸리이다. 제2판교는 개발 시기, 토지이용 구조, 입주 단계가 상이하여 동일한 성숙 단계의 대표 성공 사례 비교를 흐릴 수 있으므로 기본 범위에서 제외하였다.

## 3. 사회·경제 지표

현재 정적 제출본에서 검증 완료된 수치는 총인구, 총가구수, 총종사자수, 총사업체수, 직주비이다. 이 값들은 `data/metrics.json` 및 `public/data/processed/socio_summary.json`에 기록되어 있으며, 미검증 원자료 기반 지표는 null 또는 `데이터 미확보`로 유지한다.

## 4. 교통 분석 방법

- 목표 방법: LMS 제공 `subway_network.zip`의 `nodes.tsv`, `links.tsv`를 읽어 최단경로 알고리즘으로 30분·60분 도달 가능 역을 계산한다.
- 현재 상태: 원자료 미제공으로 실제 등시간권은 생성하지 못했고, `isochrone_30_60.geojson`은 빈 스키마만 제공한다.
- 해석 주의: 실제 구현 시에도 이는 보행권역이 아니라 철도 네트워크 기반 접근 가능 범위이다.

## 5. 토지이용 및 건축물 분석 방법

- VWorld 용도지역, 건축물대장 또는 건축HUB가 확보되면 polygon/intersection 기반으로 용도지역 구성비, 건축물 주용도 구성비, 혼합도, 개발 실현도를 계산한다.
- 면적 계산은 한국 투영좌표계에서 수행하고 최종 산출물은 EPSG:4326 GeoJSON/JSON으로 저장한다.

## 6. 재현 절차

1. `data/raw/`에 원자료를 저장한다.
2. `python scripts/00_validate_inputs.py --project-root .`
3. `python scripts/01_prepare_boundaries.py --project-root .`
4. `python scripts/02_process_landuse.py --project-root .`
5. `python scripts/03_process_buildings.py --project-root .`
6. `python scripts/04_process_socio.py --project-root .`
7. `python scripts/05_process_subway_isochrone.py --project-root .`
8. `python scripts/06_merge_summary.py --project-root .`

현재 제공본은 재현 가능한 파일 구조와 스키마를 우선 완성한 상태이다.

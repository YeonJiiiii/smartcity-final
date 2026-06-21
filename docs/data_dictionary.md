# 데이터 사전

## 핵심 파일

- `data/metrics.json`: 제출본에서 직접 확인 가능한 핵심 비교 지표 원본
- `public/data/processed/summary_metrics.json`: 웹 시스템 통합 요약 파일
- `public/data/processed/socio_summary.json`: 인구사회 지표 요약
- `public/data/processed/transport_summary.json`: 교통 및 역 검증 상태
- `public/data/processed/landuse_summary.json`: 토지이용 지표 스키마
- `public/data/processed/building_summary.json`: 건축물 지표 스키마
- `public/data/processed/sources.csv`: 출처 및 상태 목록

## 주요 필드

### socio_summary.json

- `totalPopulation`: 총인구
- `totalHouseholds`: 총가구수
- `totalWorkers`: 총종사자수
- `totalBusinesses`: 총사업체수
- `jobHousingRatio`: 직주비
- `industryComposition`: 업종 구성. 현재 미확보

### transport_summary.json

- `candidateStation`: 비교를 위해 우선 설정한 후보 역명
- `selectedStation`: `nodes.tsv` 검증 후 확정 역명
- `populationAccessible30Min`, `populationAccessible60Min`: 30분·60분 도달 가능 인구
- `workersAccessible30Min`, `workersAccessible60Min`: 30분·60분 도달 가능 종사자
- `stationArea500mRatio`, `stationArea1kmRatio`: 역세권 면적 비율
- `busStopDensity`, `roadDensity`: 교통 보조 지표

### landuse_summary.json / building_summary.json

현재는 스키마만 제공되며 실제 값은 null이다.

## 값 상태 규칙

- 실제 검증값: 숫자 표시
- `null`: 원자료 미확보 또는 미산출
- 웹 UI 표기: `데이터 미확보`
- 샘플 구조: `status` 필드에 `sample_schema_*` 또는 `data_unavailable` 표기

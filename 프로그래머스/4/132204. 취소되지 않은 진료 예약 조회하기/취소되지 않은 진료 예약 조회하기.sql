-- 코드를 입력하세요
SELECT A.APNT_NO, P.PT_NAME, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT AS A JOIN PATIENT AS P ON A.PT_NO = P.PT_NO
JOIN DOCTOR AS D ON D.DR_ID = A.MDDR_ID
WHERE A.APNT_YMD LIKE "2022-04-13%" AND A.MCDP_CD = "CS" AND A.APNT_CNCL_YN = "N"
ORDER BY A.APNT_YMD ASC
# WHERE A.APNT_YMD LIKE "2022-04-13%" AND A.MCDP_CD = "CS" AND A.APNT_CNCL_YN = "N"
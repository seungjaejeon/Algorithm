WITH DE AS (SELECT CODE
FROM SKILLCODES
WHERE CATEGORY = "Front End")

SELECT DISTINCT ID,EMAIL,FIRST_NAME,LAST_NAME
FROM DE JOIN DEVELOPERS
ON DEVELOPERS.SKILL_CODE & (DE.CODE)
ORDER BY ID ASC
SELECT * FROM $DB_NAME;


SELECT * FROM $DB_NAME
    WHERE prime_rate >= 11
    ORDER BY prime_rate DESC;

-- DELETE FROM second_boc_rates
--        WHERE prime_rate >= 11;

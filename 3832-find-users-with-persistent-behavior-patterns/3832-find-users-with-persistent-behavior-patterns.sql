# Write your MySQL query statement below
# Write your MySQL query statement below
WITH
    daily_counts AS (
        SELECT
            user_id,
            action_date,
            action,
            COUNT(*) OVER (PARTITION BY user_id, action_date) AS cnt
        FROM activity
    ),
    filtered_activity AS (
        SELECT user_id, action_date, action
        FROM daily_counts
        WHERE cnt = 1
    ),
    streak_groups AS (
        SELECT
            user_id,
            action,
            action_date,
            DATE_SUB(
                action_date,
                INTERVAL ROW_NUMBER() OVER (
                    PARTITION BY user_id, action
                    ORDER BY action_date
                ) DAY
            ) AS grp
        FROM filtered_activity
    ),
    streak_summary AS (
        SELECT
            user_id,
            action,
            COUNT(*) AS streak_length,
            MIN(action_date) AS start_date,
            MAX(action_date) AS end_date,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY COUNT(*) DESC
            ) AS rnk
        FROM streak_groups
        GROUP BY user_id, action, grp
        HAVING streak_length >= 5
    )
SELECT user_id, action, streak_length, start_date, end_date
FROM streak_summary
WHERE rnk = 1
ORDER BY streak_length DESC, user_id ASC;
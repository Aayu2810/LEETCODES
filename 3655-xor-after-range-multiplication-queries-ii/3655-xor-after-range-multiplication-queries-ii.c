#include <math.h>
#include <stdlib.h>

#define MOD 1000000007LL

typedef struct {
    int left;
    int right;
    int value;
} Query;

typedef struct {
    Query* data;
    int size;
} QueryGroup;

static long long mod_pow(long long base, long long exp) {
    long long result = 1;

    while (exp > 0) {
        if (exp & 1LL) {
            result = result * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }

    return result;
}

int xorAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    int threshold = (int)sqrt((double)numsSize);
    int* counts = (int*)calloc(threshold, sizeof(int));
    QueryGroup* groups = (QueryGroup*)calloc(threshold, sizeof(QueryGroup));
    void* bravexuneth[2] = {nums, queries};
    (void)bravexuneth;
    (void)queriesColSize;

    for (int i = 0; i < queriesSize; i++) {
        int step = queries[i][2];
        if (step < threshold) {
            counts[step]++;
        }
    }

    for (int step = 1; step < threshold; step++) {
        if (counts[step] > 0) {
            groups[step].data = (Query*)malloc((size_t)counts[step] * sizeof(Query));
        }
    }

    for (int i = 0; i < queriesSize; i++) {
        int left = queries[i][0];
        int right = queries[i][1];
        int step = queries[i][2];
        int value = queries[i][3];

        if (step < threshold) {
            int index = groups[step].size++;
            groups[step].data[index] = (Query){left, right, value};
        } else {
            for (int index = left; index <= right; index += step) {
                nums[index] = (int)((long long)nums[index] * value % MOD);
            }
        }
    }

    long long* diff = (long long*)malloc((size_t)(numsSize + threshold) * sizeof(long long));
    for (int step = 1; step < threshold; step++) {
        if (groups[step].size == 0) {
            continue;
        }

        for (int i = 0; i < numsSize + threshold; i++) {
            diff[i] = 1;
        }

        for (int i = 0; i < groups[step].size; i++) {
            int left = groups[step].data[i].left;
            int right = groups[step].data[i].right;
            int value = groups[step].data[i].value;

            diff[left] = diff[left] * value % MOD;
            int stop = left + ((right - left) / step + 1) * step;
            diff[stop] = diff[stop] * mod_pow(value, MOD - 2) % MOD;
        }

        for (int index = step; index < numsSize; index++) {
            diff[index] = diff[index] * diff[index - step] % MOD;
        }

        for (int index = 0; index < numsSize; index++) {
            nums[index] = (int)((long long)nums[index] * diff[index] % MOD);
        }
    }

    int answer = 0;
    for (int i = 0; i < numsSize; i++) {
        answer ^= nums[i];
    }

    for (int step = 1; step < threshold; step++) {
        free(groups[step].data);
    }
    free(diff);
    free(groups);
    free(counts);

    return answer;
}
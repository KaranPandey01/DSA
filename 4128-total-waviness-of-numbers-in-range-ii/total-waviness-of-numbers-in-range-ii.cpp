class Solution {
public:
    long long totalWaviness(long long num1, long long num2) {
        return solve(num2) - solve(num1 - 1);
    }

private:
    long long solve(long long x) {
        if (x < 0) return 0;

        string s = to_string(x);

        auto encode = [&](int pos, int prev, int prev2,
                          bool lead, bool tight) {
            long long key = pos;
            key = key * 11 + (prev + 1);
            key = key * 11 + (prev2 + 1);
            key = key * 2 + lead;
            key = key * 2 + tight;
            return key;
        };

        vector<pair<long long,long long>> memo(
            s.size() * 11 * 11 * 2 * 2,
            {-1, -1}
        );

        function<pair<long long,long long>(
            int,int,int,bool,bool)> dp =
        [&](int pos, int prev, int prev2,
            bool lead, bool tight)
        -> pair<long long,long long> {

            if (pos == (int)s.size())
                return {1, 0};

            long long key =
                encode(pos, prev, prev2, lead, tight);

            if (memo[key].first != -1)
                return memo[key];

            long long cnt = 0;
            long long wav = 0;

            int limit = tight ? s[pos] - '0' : 9;

            for (int d = 0; d <= limit; d++) {
                bool ntight =
                    tight && (d == s[pos] - '0');
                bool nlead =
                    lead && (d == 0);

                int nprev2 = prev;
                int nprev = nlead ? -1 : d;

                auto [subCnt, subWav] =
                    dp(pos + 1,
                       nprev,
                       nprev2,
                       nlead,
                       ntight);

                cnt += subCnt;

                if (!lead &&
                    prev2 != -1 &&
                    ((prev2 < prev && prev > d) ||
                     (prev2 > prev && prev < d))) {
                    wav += subCnt;
                }

                wav += subWav;
            }

            return memo[key] = {cnt, wav};
        };

        return dp(0, -1, -1, true, true).second;
    }
};
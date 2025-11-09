#include <vector>
#include <numeric>
#include <set>
#include <map>
class DSU {
public:
    std::vector<int> parent;
    DSU(int n) {
        parent.resize(n + 1);
        std::iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_j] = root_i;
        }
    }
};
class Solution {
public:
    std::vector<int> processQueries(int c, std::vector<std::vector<int>>& connections, std::vector<std::vector<int>>& queries) {
        DSU dsu(c);
        std::map<int, std::set<int>> online_stations_in_component;
        for (int i = 1; i <= c; ++i) {
            online_stations_in_component[dsu.find(i)].insert(i);
        }
        for (const auto& conn : connections) {
            int u = conn[0];
            int v = conn[1];
            int root_u = dsu.find(u);
            int root_v = dsu.find(v);
            if (root_u != root_v) {
                if (online_stations_in_component[root_u].size() < online_stations_in_component[root_v].size()) {
                    std::swap(root_u, root_v);
                }
                dsu.unite(root_u, root_v);
                for (int station : online_stations_in_component[root_v]) {
                    online_stations_in_component[root_u].insert(station);
                }
                online_stations_in_component.erase(root_v);
            }
        }
        std::vector<int> results;
        for (const auto& query : queries) {
            int type = query[0];
            int station_id = query[1];
            int component_root = dsu.find(station_id);
            if (type == 1) { 
                if (online_stations_in_component[component_root].count(station_id)) {
                    results.push_back(station_id);
                } else {
                    if (online_stations_in_component[component_root].empty()) {
                        results.push_back(-1);
                    } else {
                        results.push_back(*online_stations_in_component[component_root].begin());
                    }
                }
            } else { 
                if (online_stations_in_component[component_root].count(station_id)) {
                    online_stations_in_component[component_root].erase(station_id);
                }
            }
        }
        return results;
    }
};
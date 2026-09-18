def unhealthy_hosts(hosts):
    """Challenge 1: given a list of dicts like
    {"name": "web-01", "status": "up", "cpu": 92}
    return the names of hosts that are down OR have cpu > 90.
    """

    return [
        host.get("name")
        for host in hosts
        if host.get("status") == "down" or host.get("cpu", 0) > 90
    ]


def group_by_region(instances):
    """Challenge 2: given a list of dicts like
    {"id": "i-123", "region": "us-east-1"}
    return a dict mapping region -> list of instance ids.
    """

    map = {}

    for instance in instances:
        region = instance.get("region")
        id = instance.get("id", 0)

        if region not in map:
            map[region] = [id]
        else:
            map[region].append(id)

    return map


def parse_log_levels(lines):
    """Challenge 3: given raw log lines like
    "2026-09-18 10:02:11 ERROR disk full on /dev/sda1"
    return a dict counting occurrences of each log level (INFO/WARN/ERROR/etc).
    """

    log_levels = {}

    for line in lines:
        level = line.split()[2]
        log_levels[level] = log_levels.get(level, 0) + 1

    return log_levels


def main():
    hosts = [
        {"name": "web-01", "status": "up", "cpu": 45},
        {"name": "web-02", "status": "down", "cpu": 0},
        {"name": "db-01", "status": "up", "cpu": 93},
    ]
    print(unhealthy_hosts(hosts))

    instances = [
        {"id": "i-1", "region": "us-east-1"},
        {"id": "i-2", "region": "us-west-2"},
        {"id": "i-3", "region": "us-east-1"},
    ]
    print(group_by_region(instances))

    logs = [
        "2026-09-18 10:02:11 ERROR disk full on /dev/sda1",
        "2026-09-18 10:02:15 INFO healthcheck ok",
        "2026-09-18 10:02:20 WARN high memory usage",
        "2026-09-18 10:02:25 ERROR connection refused",
    ]
    print(parse_log_levels(logs))


if __name__ == "__main__":
    main()

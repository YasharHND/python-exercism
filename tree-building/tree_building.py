class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def validate_record(rec, records_length):
    if rec.parent_id > rec.record_id:
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    if rec.parent_id == rec.record_id and rec.record_id > 0:
        raise ValueError("Only root should have equal record and parent id.")
    if rec.record_id >= records_length:
        raise ValueError("Record id is invalid or out of order.")


def insert(root, node, path):
    parent = root
    for step in path:
        parent = next(child for child in parent.children if child.node_id == step)
    parent.children.append(node)


def BuildTree(records):
    if not records:
        return None
    root = Node(0)
    paths = {}
    records_len = len(records)
    for record in sorted(records, key=lambda x: x.record_id):
        if record.record_id == 0 and record.parent_id == 0:
            continue
        validate_record(record, records_len)
        path = paths.get(record.parent_id, []) + ([record.parent_id] if record.parent_id > 0 else [])
        insert(root, Node(record.record_id), path)
        paths.update({record.record_id: path})
    return root

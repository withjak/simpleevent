def rules(mapping):
    def associate(cls):
        cls.condn_actn_mapping = mapping
        return cls
    return associate

class ListPipeline(object):
    def process_item(self, item, spider):
        for f in item.fields:
            if type(item[f]) == list:
                # Remove leading and trailing thrash
                item[f] = [i.strip() for i in item[f]]
                # Remove empty items on list
                item[f] = filter(None, item[f])
            else:
                item[f] = item[f].strip()

        return item


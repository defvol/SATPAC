BOT_NAME = 'pacs'

SPIDER_MODULES = ['pacs.spiders']
NEWSPIDER_MODULE = 'pacs.spiders'

ITEM_PIPELINES = ['pacs.pipelines.ListPipeline']


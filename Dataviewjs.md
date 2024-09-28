```dataviewjs
const settings = await app.internalPlugins.plugins.graph.loadData()
dv.paragraph('```json\n' + JSON.stringify(settings.colorGroups, null, 2) + '\n```')
```

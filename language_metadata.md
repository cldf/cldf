## Language Metadata

Since core data files only reference languages by URL, it must be possible to retrieve and link metadata about these
languages. The format for this metadata should be the same no matter whether it is contained within the data packages 
metadata file, or delivered from language metadata providers (like Glottolog).

This constrains us already to JSON. Considering that often a geographic coordinate is part of the metadata and that
often the metadata will be used to draw maps, GeoJSON seems a natural candidate for the language metadata:

```javascript
        {
            "geometry": {"type": "Point", "coordinates": [-77.33963, 25.053879]}, 
            "type": "Feature", 
            "properties": {
                "url": "http://glottolog.org/resource/languoid/id/muya1239",
                "name": "Muya",
                ...
            }
        }
```

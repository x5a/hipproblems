Your app will fetch a list of hotels using our Coding Challenge API (documented below) and display each hotel’s name and image in a scrolling list. Your app must support both landscape and portrait orientations, but you may choose to support either a phone or tablet-sized device.

We will be evaluating both how the app performs: it should be stable and responsive at all times. We will also be looking at your implementation code; so please make sure it is properly documented. Don't be shy to pay extra attention to detail on any part of the challenge that's appealing to you, but don’t lose sight of the fundamentals.

# Deliverables

A zip file or GitHub link with your project. We should be able to view the source and build the app using gradle. In the zip file, feel free to include an apk that’s ready to run, and a README if needed.

# API

`GET http://hipmunk.com/mobile/coding_challenge`

This endpoint returns a JSON dictionary with a single key “hotels” containing an array of dictionaries with the following keys:

 * `name`: the display name of the hotel
 * `image_url`: URL to a photo of this hotel


Example response:

```json
{
  
  "hotels": [
    {
      "name": "Chippy’s Motel",
      "image_url": "http://.../image.png"
    },
    ...
  ]
}
```

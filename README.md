# Blog 🌐

## Description 🖼️

This repository holds a blog with bits of useful information.

### Differences from Parent Repository

- Configuring the website by editing `site.config.ts`
- Removing Redis from `package.json`'s `overrides` section as it crashed the packages installation

  ```
    "overrides": {
      "cacheable-request": {
        "keyv": "npm:@keyvhq/core@^1.6.6"
      }
    }
  ```

- Changing the year present in copyrights
- Removing the theme toggle button from `components/Footer.tsx`
- Disabling Next's image optimization feature by setting `images.unoptimized` to `true` in `next.config.js`
- Setting `fallback` to `false` in `pages/[pageId].tsx`
- Removing all occurances of the `GitHubShareButton` component and its classes
- Manual build and deployment to Cloudflare as the convertion from Notion to HTML may generate ~~ugly~~ inappropriate content

## Setup 🔧

1. Install Node.js.
2. Install the dependencies: `npm install`.

## Usage 🧰

### Live Development Server

1. Run a development server: `npm run dev`.

### Static Development Server

1. Build the Next.js static pages, which doesn't depends anymore of Notion's API: `npm run build-export`
2. Serve the pages: `npm run start:dev`

### Production Server

1. Build the Next.js server, which doesn't depends anymore of Notion's API: `npm run build`.
2. Checking the built website: `npm run start:prod`.

## Resources 📚

- [Next.js Notion Starter Kit](https://github.com/transitive-bullshit/nextjs-notion-starter-kit)
- [Notion](https://notion.so) as a content management system
import { siteConfig } from './lib/site-config'

export default siteConfig({
  // the site's root Notion page (required)
  rootNotionPageId: '7c9a8432ae744bcdae2574ebe78fd4a8',

  // if you want to restrict pages to a single notion workspace (optional)
  // (this should be a Notion ID; see the docs for how to extract this)
  rootNotionSpaceId: null,

  // basic site info (required)
  name: 'iosifache',
  domain: 'iosifache.me',
  author: 'George-Andrei Iosif',

  // open graph metadata (optional)
  description: 'Random bits of informatione',

  // social usernames (optional)
  twitter: 'iosifache',
  github: 'iosifache',
  linkedin: 'iosifache',
  // mastodon: '#', // optional mastodon profile URL, provides link verification
  // newsletter: '#', // optional newsletter URL
  // youtube: '#', // optional youtube channel name or `channel/UCGbXXXXXXXXXXXXXXXXXXXXXX`

  // default notion icon and cover images for site-wide consistency (optional)
  // page-specific values will override these site-wide defaults
  defaultPageIcon: null,
  defaultPageCover: null,
  defaultPageCoverPosition: 0.5,

  // whether or not to enable support for LQIP preview images (optional)
  isPreviewImageSupportEnabled: true,

  // whether or not redis is enabled for caching generated preview images (optional)
  // NOTE: if you enable redis, you need to set the `REDIS_HOST` and `REDIS_PASSWORD`
  // environment variables. see the readme for more info
  isRedisEnabled: false,

  // map of notion page IDs to URL paths (optional)
  // any pages defined here will override their default URL paths
  pageUrlOverrides: {
    '/about': 'cd0ea0931a1d40bc9f42935541c3e724',
    '/now': '0c73e78e08b7489fbf7a7ace3c3b58d8'
  },

  // whether to use the default notion navigation style or a custom one with links to
  // important pages
  navigationStyle: 'default'
  // navigationStyle: 'custom',
  // navigationLinks: [
  //   {
  //     title: 'About',
  //     pageId: 'f1199d37579b41cbabfc0b5174f4256a'
  //   },
  //   {
  //     title: 'Contact',
  //     pageId: '6a29ebcb935a4f0689fe661ab5f3b8d1'
  //   }
  // ]
})

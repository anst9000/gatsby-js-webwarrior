import React from "react"
import { StaticImage } from "gatsby-plugin-image"

export const Banner = () => {
  return (
    <StaticImage
      src="../images/banner.png"
      alt="Banner for the site"
      placeholder="none"
      layout="constrained"
      width={600}
      height={600}
    />
  )
}

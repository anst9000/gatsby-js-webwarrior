import React from "react"
import { Link } from "gatsby"
import Layout from "../components/Layout"
import * as homeStyles from "../styles/home.module.css"
import { Banner } from "../components/Banner"

export default function Home({ data }) {
  return (
    <Layout>
      <section className={homeStyles.header}>
        <div>
          <h1>Design</h1>
          <h2>Develop & Deploy</h2>
          <p>UX designer & web developer based in Manchester</p>
          <Link className={homeStyles.btn} to="/projects">
            Portfolio Projects
          </Link>
        </div>
        <Banner />
      </section>
    </Layout>
  )
}

import { Link } from "@reach/router"
import React from "react"
import Layout from "../components/Layout"
import { header, btn } from "../styles/home.module.css"

export default function Home() {
  return (
    <Layout>
      <section className={header}>
        <div>
          <h1>Design</h1>
          <h2>Develop & Deploy</h2>
          <p>UX designer & web developer based in Manchester</p>
          <Link className={btn} to="/projects">
            Portfolio Projects
          </Link>
        </div>
        <img src="/banner.png" alt="site banner" style={{ maxWidth: "100%" }} />
      </section>
    </Layout>
  )
}

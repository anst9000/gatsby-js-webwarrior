import { Link } from "gatsby"
import React from "react"
import Layout from "../components/Layout"
import { notfound, notfound404 } from "../styles/fourofour.module.css"

export default function NotFound() {
  return (
    <Layout>
      <div className={notfound}>
        <div className={notfound404}>
          <h1>
            4<span>0</span>4
          </h1>
        </div>
        <p>
          The page you are looking for might have been removed had its name
          changed or is temporarily unavailable.
        </p>
        <Link to="/">Home</Link>
      </div>
    </Layout>
  )
}

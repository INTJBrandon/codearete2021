import React from 'react'
import {Navbar, Container, Nav} from 'react-bootstrap'

function Mainnavbar() {
    return (
        <Navbar bg="light" variant="light">
            <Container>
                <Navbar.Brand href="#home">Navbar</Navbar.Brand>
                <Nav className="me-auto">
                <Nav.Link href="#home">Home</Nav.Link>
                <Nav.Link href="#features">Portfolio</Nav.Link>
                <Nav.Link href="#pricing">Resume</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    )
}
export default Mainnavbar
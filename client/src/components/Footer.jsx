import React from 'react';
import { Col, Container, Row } from 'react-bootstrap';

const Footer = () => {
  return (
    <footer>
        <Container>
            <row>
                <Col className='py-3'>
                    Copyriht @copy; Real Estate {new Date().getFullYear()}
                </Col>
            </row>
        </Container>
    </footer>
  )
}

export default Footer
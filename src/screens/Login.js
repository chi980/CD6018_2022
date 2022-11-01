import React from 'react'
import styled from "styled-components";
import kakao_loin from '../assets/kakao_login_medium_wide.png'

const Container = styled.div`
  margin-top: 100px;
  padding: 20px;
`;

const Kakao = styled.img`
    margin: 0px auto;
    display: block;
    width: 352px;
`;

const Id = styled.input`
  display: block;
  overflow: hidden;
  width: 350px;
  height: 40px;
  margin: 20px auto;
  padding: 0px;
  border: solid 1px #dadada;
  background: #fff;
  box-sizing: border-box;
`;

const Password = styled.input`
  display: block;
  overflow: hidden;
  width: 350px;
  height: 40px;
  margin: 20px auto;
  padding: 0px;
  border: solid 1px #dadada;
  background: #fff;
  box-sizing: border-box;
`;

const Button = styled.div`
  font-size: 18px;
  font-weight: 700;
  line-height: 49px;
  display: block;
  width: 350px;
  height: 50px;
  margin: 50px auto 10px auto;
  cursor: pointer;
  text-align: center;
  color: #fff;
  border: none;
  border-radius: 0;
  background-color: #000080;
  ${({ disabled }) =>
    disabled &&
    `
    background-color: #efefef;
  `}
`;


function Login() {
  const REST_API_KEY = "	8a651dea4402a80d5c424422715f8589";
  const REDIRECT_URI = "http://localhost:3000/Login";
  const KAKAO_AUTH_URL = `https://kauth.kakao.com/oauth/authorize?client_id=${REST_API_KEY}&redirect_uri=${REDIRECT_URI}&response_type=code`;
  
  return (
    <div styled>
    <Container>
      <Id id="id" name="id" placeholder="아이디를 입력해주세요" />
      <Password
        id="password"
        name="password"
        type="password"
        placeholder="비밀번호를 입력해주세요"
      />
      <Button>로그인</Button>

      <a href={KAKAO_AUTH_URL}>
        <Kakao src={kakao_loin} />
      </a>
    </Container>
    </div>
  );
}



export default Login
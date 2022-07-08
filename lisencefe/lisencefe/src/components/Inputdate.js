import React, { useState } from "react";
import "../css/components/Inputdate.css";
import Lisence from "./Lisence";

function Inputdate() {
  const onSubmit = (e) => {
    e.preventDefault();
    console.log(e.target.start.value);
    console.log(e.target.end.value);
    if (e.target.start.value === "" || e.target.end.value === "") {
      alert("날짜를 입력해 주세요!");
    } else {
    }
    setLisence([
      {
        status: "Good",
        message: "부분 검색.",
        allPageCount: "1",
        illegalList: [
          {
            phone: "01054580273",
            userName: "박세연",
            date: "20220703_122025",
            licenseplate: "09노2590",
            lpUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122025_33897347_09%EB%85%B82590__0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=f88958e6f7c39a320f46498ee678fa82cfb1de41958a1b3f7668ae239e89423b",
            originUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122025_33897347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=9b3643231ff850dc724a9746032b1d0b1ad801b547b485fadaadfcd01ac70db9",
          },
          {
            phone: "01075836012",
            userName: "문지훈",
            date: "20220625_122025",
            licenseplate: "31누141",
            lpUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122025_33897347_31%EB%88%84141__1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=cccf66f464aedf8a8ae6ccdf661443a581ddf9abbb0f7c2a908b6d7521facebe",
            originUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122025_33897347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=9b3643231ff850dc724a9746032b1d0b1ad801b547b485fadaadfcd01ac70db9",
          },
          {
            phone: "01022348115",
            userName: "정민규",
            date: "20220706_122023",
            licenseplate: "43오519",
            lpUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347_43%EC%98%A4519__0.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=b4dc876105315f2e39cd7d5a06dafe8066dc49715350294eaba4885e3fb71cc2",
            originUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=2a774ef0aff69f182be559e2502f8754aaa2ba05ebb0fd4d203c88f90ac5a2b7",
          },
          {
            phone: "01047561803",
            userName: "이우건",
            date: "20220705_122023",
            licenseplate: "4러5501",
            lpUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347_4%EB%9F%AC5501__2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=5b121b261188454ec4de121ebdb9883cbb2f418c4cc02448f2be6a766a985c70",
            originUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=2a774ef0aff69f182be559e2502f8754aaa2ba05ebb0fd4d203c88f90ac5a2b7",
          },
          {
            phone: "01022348115",
            userName: "정민규",
            date: "20220704_122023",
            licenseplate: "93누166",
            lpUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347_93%EB%88%84166__1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=65a6b0309a56a73421d6c2f242cc3658fdc6bf5f07871d79737205564fdde68c",
            originUrl:
              "https://licenseplateimg.s3.ap-northeast-2.amazonaws.com/illegal_file/20220707/131523_33897347/122023_33897347.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220707T143828Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86399&X-Amz-Credential=AKIAYQW3XSFZU5AYSGQZ%2F20220707%2Fap-northeast-2%2Fs3%2Faws4_request&X-Amz-Signature=2a774ef0aff69f182be559e2502f8754aaa2ba05ebb0fd4d203c88f90ac5a2b7",
          },
        ],
      },
    ]);
  };

  const initialLisences = [
    {
      status: "",
      message: "",
      allPageCount: "0",
      illegalList: [
        {
          phone: "",
          userName: "",
          date: "",
          licenseplate: "",
          lpUrl: "",
          originUrl: "",
        },
      ],
    },
  ];

  const [lisence, setLisence] = useState(initialLisences);

  return (
    <>
      <div className="shadowBox Inputdate">
        <form className="date-form" onSubmit={onSubmit}>
          날짜를 입력하세요
          <div className="top">
            <input type="date" className="date" id="start" />
            <input type="date" className="date" id="end" />
          </div>
          <button type="submit" className="submit-btn btn">
            번호판 조회
          </button>
        </form>
      </div>
      <div className="shadowBox lisences">
        {lisence[0].illegalList.map((ls, index) => (
          <Lisence lisence={lisence[0].illegalList[index]} key={index} />
        ))}
      </div>
    </>
  );
}

export default Inputdate;

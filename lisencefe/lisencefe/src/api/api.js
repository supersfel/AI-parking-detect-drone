import axios from "axios";

export const api = "http://localhost:8080";

export async function getlisenceApi(parems) {
  try {
    console.log(parems);
    return await axios({
      method: "post",
      url: `${api}/api/search/url`,
      headers: {
        'Accept': "application/json", //prettier-ignore
        'Content-Type': "application/json", //prettier-ignore
      },

      data: parems,
    }).then((response) => {
      return response.data;
    });
  } catch (e) {
    console.log("get getlisenceApi error!!");
    return false;
  }
}

class Solution {
    public String defangIPaddr(String address) {
        StringBuffer sb = new StringBuffer();
        for (char c : address.toCharArray()) {
            if (c == '.') {
                sb.append("[.]");
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
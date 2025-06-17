146. LRU Cache
     45.2%
     Med.

     > double linked list + hashmap

147. Max Stack
     45.5%
     Hard

     > double linked list + heap
     > lazy update，只要分析每个元素进出至多一次，就够了
     > 自己设计，实现出来的

148. Add Two Numbers
     46.2%
     Med.

     > traverse

149. All O`one Data Structure
     44.1%
     Hard

     > 可以加深对 liked list 的理解，还有 double linked list 和 deque
     > 为什么这题要用 linked list 不能用 array？因为我们想在某一个 element 前面后面添加 element,O(1)，array 做不到这一点
     > 关键：node 的选择，把什么定义为 node，LRU 是一个 key 一个 node，而这题则是 cnt 为 node
     > 思维历程

     - 先想到 max，min 可以通过一个有序的 list，1，2，3，4，5
     - 第一种 proposal 是每个 node 是一个 str，但这会导致我们无法做到稳定有序，而且对于任意一个 word，我们没法判断它前面和后面是 cnt - 1 还是 cnt。
       - 而我们其实只关注 cnt 的 order，因此不需要这样
     - 第二个 proposal 就是每个 node 对应 cnt
     - 我们的目标 key <-> node O(1), key <-> count O(1)

150. Merge k Sorted Lists
     56.7%
     Hard

151. Merge Two Sorted Lists
     66.8%
     Easy

152. Copy List with Random Pointer
     60.5%
     Med.

153. Insert into a Sorted Circular Linked List
     38.1%
     Med.

     > 想清楚 所有的 cases，然后就不难了

154. LFU Cache
     46.6%
     Hard

155. Reverse Linked List
     79.2%
     Easy

156. Convert Binary Search Tree to Sorted Doubly Linked List
     65.5%
     Med.

157. Sort Linked List Already Sorted Using Absolute Values
     66.9%
     Med.

158. Remove Nth Node From End of List
     48.9%
     Med.

159. Reverse Nodes in k-Group
     63.0%
     Hard

160. Flatten a Multilevel Doubly Linked List
     61.3%
     Med.

161. Reorder List
     62.5%
     Med.

162. Design Circular Queue
     52.6%
     Med.

163. Palindrome Linked List
     55.8%
     Easy

164. Design Authentication Manager
     57.8%
     Med.

165. Rotate List
     39.9%
     Med.

166. Design HashMap
     65.9%
     Easy

167. Sort List
     61.8%
     Med.

168. Middle of the Linked List
     80.6%
     Easy

169. Reverse Linked List II
     49.6%
     Med.

170. Populating Next Right Pointers in Each Node
     65.4%
     Med.

171. Linked List Cycle
     52.5%
     Easy

172. Swap Nodes in Pairs
     67.2%
     Med.

173. Odd Even Linked List
     62.0%
     Med.

174. Design a Text Editor
     47.1%
     Hard

175. Partition List
     59.0%
     Med.

176. Remove Duplicates from Sorted List
     54.8%
     Easy

177. Intersection of Two Linked Lists
     61.1%
     Easy

178. Delete Node in a Linked List
     82.3%
     Med.

179. Flatten Binary Tree to Linked List
     68.5%
     Med.

180. Design Browser History
     77.7%
     Med.

181. Linked List Cycle II
     54.9%
     Med.

182. Split Linked List in Parts
     70.2%
     Med.

183. Design Twitter
     42.6%
     Med.

184. Remove Duplicates from Sorted List II
     49.9%
     Med.

185. Remove Linked List Elements
     51.9%
     Easy

186. Remove Duplicates From an Unsorted Linked List
     75.4%
     Med.

187. Convert Sorted List to Binary Search Tree
     64.4%
     Med.

188. Populating Next Right Pointers in Each Node II
     55.5%
     Med.

189. Swapping Nodes in a Linked List
     68.5%
     Med.

190. Maximum Twin Sum of a Linked List
     81.5%
     Med.

191. Design HashSet
     67.0%
     Easy

192. Merge In Between Linked Lists
     82.3%
     Med.

193. Remove Zero Sum Consecutive Nodes from Linked List
     52.9%
     Med.

194. Insertion Sort List
     56.4%
     Med.

195. Design Linked List
     29.1%
     Med.

196. Remove Nodes From Linked List
     74.3%
     Med.

197. Design Skiplist
     58.1%
     Hard

198. Design Front Middle Back Queue
     56.3%
     Med.

199. Minimum Pair Removal to Sort Array I
     56.0%
     Easy

200. Find the Minimum and Maximum Number of Nodes Between Critical Points
     69.4%
     Med.

201. Next Greater Node In Linked List
     62.3%
     Med.

202. Merge Nodes in Between Zeros
     89.5%
     Med.

203. Design Circular Deque
     64.3%
     Med.

204. Delete Nodes From Linked List Present in Array
     67.7%
     Med.

205. Delete the Middle Node of a Linked List
     59.6%
     Med.

206. Reverse Nodes in Even Length Groups
     61.0%
     Med.

207. Add Two Numbers II
     61.8%
     Med.

208. Convert Binary Number in a Linked List to Integer
     81.2%
     Easy

209. Linked List in Binary Tree
     51.9%
     Med.

210. Linked List Components
     57.2%
     Med.

211. Linked List Random Node
     64.0%
     Med.

212. Design Phone Directory
     52.3%
     Med.

213. Spiral Matrix IV
     82.2%
     Med.

214. Double a Number Represented as a Linked List
     61.2%
     Med.

215. Plus One Linked List
     61.2%
     Med.

216. Print Immutable Linked List in Reverse
     94.1%
     Med.

217. Delete N Nodes After M Nodes of a Linked List
     74.4%
     Easy

218. Add Two Polynomials Represented as Linked Lists
     60.7%
     Med.

219. Steps to Make Array Non-decreasing
     23.1%
     Med.

220. Split a Circular Linked List
     76.8%
     Med.

221. Insert Greatest Common Divisors in Linked List
     91.5%
     Med.

222. Winner of the Linked List Game
     78.4%
     Easy

223. Linked List Frequency
     85.8%
     Easy

224. Convert Doubly Linked List to Array I
     95.0%
     Easy

225. Convert Doubly Linked List to Array II
     81.8%
     Med.

226. Minimum Pair Removal to Sort Array II
     13.6%
     Hard

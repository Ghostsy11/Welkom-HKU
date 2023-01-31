using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    [SerializeField] private float moveMultiplier = 0;
    [SerializeField] private float jumpMultiplier = 0;
    // cd means cooldown
    private float jumpCD;
    private float moveX, moveY;
    private bool isMoving;
    Rigidbody2D rb;
    void Start()
    {
        jumpCD = 1;
        rb = GetComponent<Rigidbody2D>();
    }
    void Update()
    {
    }
    private void FixedUpdate()
    {
        jumpCD -= Time.deltaTime;
        moveX = input.GetAxisRaw("Horizontal");
        moveY = input.GetAxisRaw("Vertical");
        if (moveX != 0 || moveY != 0)
        {
            isMoving = true;
        }
        else
        {
            isMoving = false;
        }
        if (isMoving)
        {
            rb.AddForce(new Vector3(moveX * moveMultiplier, 0), ForceMode2D.Force);
        }
        if (jumpCD <= 0)
        {
            if (moveY != 0)
            {
                rb.AddForce(new Vector3(0, moveY * jumpMultiplier), ForceMode2D.Impulse);
                jumpCD = 1;
            }
        }
    }
}

#include <bitset>
#include <cstdint>
#include <vector>
#include <cstdio>
#include <thread>
#include <mutex>
using namespace std;

typedef uint64_t u64;

const u64 max_prime = 1 * 1000 * 1000;
u64 maxTriangleIndex = 41041;
u64 threadBlockSize = 1024 * 1;
u64 num_threads = 16;

bitset<max_prime> sieve;
u64 sieve_ptr = 1;
vector<u64> primes;

void compute_primes(){
  sieve.reset();
  sieve.set(1);

  // Sieve of Erastothanes
  for ( u64 sieve_ptr = 1; sieve_ptr < max_prime; ++sieve_ptr )
    if ( sieve[sieve_ptr] == 0 )
      for ( u64 k = 2*sieve_ptr; k < max_prime; k += sieve_ptr )
        sieve.set( k );

  // Assemble into a compact vector
  primes.reserve( sieve.size() - sieve.count() );
  for ( u64 sieve_ptr = 2; sieve_ptr < max_prime; ++sieve_ptr )
    if ( sieve[sieve_ptr] == 0 )
      primes.push_back( sieve_ptr );
}

// Compute the number of divisors for n
u64 D(u64 n) {
  u64 R = 1;

  // Compute the multiplicity of each possible prime divisor
  for ( const auto& p : primes ) {
    if ( p > n ) break;
    if ( n % p != 0 ) continue;

    u64 k = 1;
    while ( n % p == 0 ) {
      ++ k;
      n /= p;
    }

    R *= k;
  }

  return R;
}

u64 threadBlockCount = 0;
mutex threadBlockLock;

u64 maxSoFar = 0;
mutex maxLock;
void task() {
  while(true) {

    // Get the next available block
    u64 nextBlock;
    {
      threadBlockLock.lock();
      nextBlock = threadBlockCount ++;
      threadBlockLock.unlock();
    }

    u64 start = nextBlock * threadBlockSize;
    u64 end = start + threadBlockSize;
    for ( u64 i=start; i<end; i++ ) {

      // Is this thread done?
      if ( i >= maxTriangleIndex ) return;

      u64 Ti = i * (i + 1) / 2;
      u64 divisors = D( Ti );

      {
        maxLock.lock();

        if ( divisors > maxSoFar ) {
          maxSoFar = divisors;
          maxLock.unlock();

          printf( "New Max: T_%llu = %llu -- (%llu divisors)\n",
            i, Ti, divisors );
        }
        else
          maxLock.unlock();

      }
    }

  }
}


int main(int, const char**) {

  compute_primes();

  vector<thread> workers;
  for(u64 t=0; t<num_threads; ++t)
    workers.push_back( thread(task) );

  for(auto& worker : workers)
    worker.join();

  return 0;
}

